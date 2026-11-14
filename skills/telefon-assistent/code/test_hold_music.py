import importlib
import math
import struct
import unittest

SILENCE=b'\0'*320

def rms(pcm):
    values=struct.unpack('<160h',pcm)
    return math.sqrt(sum(v*v for v in values)/len(values))

class HoldMusicTests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(importlib.util.find_spec('hold_music'),'Waiting music is not implemented yet')
        self.music=importlib.import_module('hold_music').HoldMusic()
    def ready(self):
        self.music.render(SILENCE,waiting=True,now=0)
        for i in range(20): out=self.music.render(SILENCE,waiting=True,now=3+i*.02)
        return out
    def test_no_music_without_a_pending_job(self):
        self.assertEqual(self.music.render(SILENCE,waiting=False,now=5),SILENCE)
    def test_short_lookups_remain_quiet(self):
        self.music.render(SILENCE,waiting=True,now=0)
        self.assertEqual(self.music.render(SILENCE,waiting=True,now=1.9),SILENCE)
        self.assertGreater(rms(self.ready()),30)
    def test_loop_is_quiet_telephone_pcm_and_bounded(self):
        self.ready(); peak=0
        for i in range(800):
            pcm=self.music.render(SILENCE,waiting=True,now=4+i*.02)
            self.assertEqual(len(pcm),320)
            peak=max(peak,max(abs(v) for v in struct.unpack('<160h',pcm)))
        self.assertGreater(peak,100); self.assertLess(peak,1500)
    def test_user_voice_stops_music_immediately_and_it_waits_before_resuming(self):
        self.ready(); self.music.user_spoke(4)
        self.assertEqual(self.music.render(SILENCE,waiting=True,now=4),SILENCE)
        self.assertEqual(self.music.render(SILENCE,waiting=True,now=4.8),SILENCE)
        self.assertGreater(rms(self.music.render(SILENCE,waiting=True,now=5.2)),0)
    def test_assistant_speech_is_not_mixed_with_music(self):
        self.ready(); speech=struct.pack('<160h',*([2500,-2500]*80))
        self.assertEqual(self.music.render(speech,waiting=True,now=4),speech)
        self.assertEqual(self.music.render(SILENCE,waiting=True,now=4.4),SILENCE)
    def test_completed_cancelled_or_closing_work_has_no_music_tail(self):
        self.ready()
        self.assertEqual(self.music.render(SILENCE,waiting=False,now=4),SILENCE)
        self.ready()
        self.assertEqual(self.music.render(SILENCE,waiting=True,now=4,muted=True),SILENCE)

if __name__=='__main__': unittest.main()
