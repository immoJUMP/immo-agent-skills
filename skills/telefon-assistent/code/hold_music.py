"""Original quiet playful swing loop, played locally only while a phone job waits."""
from functools import lru_cache
import math
import struct

RATE=8000
FRAME_SAMPLES=160


@lru_cache(maxsize=1)
def music_loop():
    # Original jaunty swing tune, not a transcription of an existing recording.
    beat=60/160; length=32*beat
    chords=((60,64,67,69),(57,61,64,67),(62,65,69,72),(55,59,62,65),
            (64,68,71,74),(57,60,64,67),(62,66,69,72),(55,59,62,65))
    melody=((79,76,81,79,74),(76,73,79,76,69),(77,81,84,81,77),(74,77,71,74,79),
            (80,83,86,83,76),(81,76,72,76,79),(78,81,84,78,74),(77,74,71,74,79))
    events=[]
    for bar,(chord,notes) in enumerate(zip(chords,melody)):
        for offset,note,duration in zip((0,.667,1.5,2.667,3.5),notes,(.48,.55,.72,.48,.35)):
            events.append(('reed',(bar*4+offset)*beat,duration*beat,(note,)))
        for offset,note in enumerate((chord[0]-24,chord[2]-24,chord[0]-12,chord[2]-24)):
            events.append(('bass',(bar*4+offset)*beat,.62*beat,(note,)))
        for offset in (1,3):
            events.append(('chord',(bar*4+offset)*beat,.30*beat,chord))
        for offset in (0,.667,1,1.667,2,2.667,3,3.667):
            events.append(('brush',(bar*4+offset)*beat,.10*beat,()))
    samples=[0.0]*round(RATE*length)
    for kind,start,duration,notes in events:
        frequencies=[440*2**((note-69)/12) for note in notes]
        for j in range(round(duration*RATE)):
            t=j/RATE; phase=t/duration
            envelope=min(1,t/.008)*min(1,(duration-t)/.025)
            if kind=='reed':
                f=frequencies[0]; angle=2*math.pi*f*t+.012*math.sin(2*math.pi*5*t)
                sound=430*(math.sin(angle)+.30*math.sin(3*angle)+.10*math.sin(5*angle))*envelope*(1-.3*phase)
            elif kind=='bass':
                angle=2*math.pi*frequencies[0]*t
                sound=260*(math.sin(angle)+.4*math.sin(2*angle))*envelope*math.exp(-3*phase)
            elif kind=='chord':
                sound=sum(math.sin(2*math.pi*f*t)+.2*math.sin(4*math.pi*f*t) for f in frequencies)*75*envelope*math.exp(-4*phase)
            else:
                # Deterministic soft brush tick; no external audio asset.
                noise=((j*1103515245+12345)%65536)/32768-1
                sound=65*noise*envelope*math.exp(-8*phase)
            samples[(round(start*RATE)+j)%len(samples)]+=sound
    return tuple(round(sample) for sample in samples)


class HoldMusic:
    def __init__(self):
        self.samples=music_loop(); self.position=0; self.gain=0
        self.waiting_since=None; self.last_user=-math.inf; self.last_voice=-math.inf
        self.audible=False
    def user_spoke(self,now): self.last_user=now
    def render(self,pcm,*,waiting,now,muted=False):
        values=struct.unpack('<160h',pcm)
        rms=math.sqrt(sum(x*x for x in values)/FRAME_SAMPLES)
        if rms>180: self.last_voice=now
        if not waiting: self.waiting_since=None
        elif self.waiting_since is None: self.waiting_since=now
        eligible=(waiting and not muted and now-self.waiting_since>=2 and
                  now-self.last_user>=1 and now-self.last_voice>=.7)
        self.audible=eligible
        if not eligible:
            self.gain=0
            return pcm  # Never mix over either speaker, a completed job or hangup.
        target=min(1,self.gain+.1); out=[]
        for i,voice in enumerate(values):
            gain=self.gain+(target-self.gain)*(i+1)/FRAME_SAMPLES
            music=self.samples[(self.position+i)%len(self.samples)]
            out.append(max(-32768,min(32767,round(voice+music*gain))))
        self.position=(self.position+FRAME_SAMPLES)%len(self.samples); self.gain=target
        return struct.pack('<160h',*out)
