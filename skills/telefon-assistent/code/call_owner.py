"""Owner-only phone client: call, schedule, inspect and cancel. No arbitrary recipients."""
import argparse
from datetime import datetime
import json
import os
from pathlib import Path
import urllib.error
import urllib.request
import uuid
from zoneinfo import ZoneInfo


def request(cfg,base,path,body=None):
    req=urllib.request.Request(base+path,data=json.dumps(body).encode() if body is not None else None,
        headers={'Authorization':'Bearer '+cfg['token'],'Content-Type':'application/json'})
    with urllib.request.urlopen(req,timeout=45) as response: return json.load(response)


def main():
    parser=argparse.ArgumentParser()
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--reason')
    group.add_argument('--status',action='store_true')
    group.add_argument('--check',action='store_true',help='Validate chat access without calling or scheduling')
    group.add_argument('--tasks',action='store_true')
    group.add_argument('--cancel',metavar='CALL_ID')
    group.add_argument('--hangup',metavar='CALL_ID')
    group.add_argument('--schedule-cancel',metavar='EVENT_ID')
    group.add_argument('--routines',metavar='OFF_OR_HH:MM')
    group.add_argument('--calendar-preparation',choices=['on','off'])
    parser.add_argument('--event-id')
    parser.add_argument('--kind',choices=['requested','proactive','emergency','info','decision'],default='requested')
    parser.add_argument('--mode',choices=['conversation','preparation','sales_training','daily_review'],default='conversation')
    parser.add_argument('--evidence',default='')
    parser.add_argument('--deadline')
    parser.add_argument('--at',help='ISO time with timezone; schedule one call')
    parser.add_argument('--before-meeting',action='store_true',help='Call 15 minutes before --at')
    parser.add_argument('--session-id')
    args=parser.parse_args()
    cfg=json.loads((Path(os.environ.get('HERMES_HOME','/opt/data'))/'telephony-client.json').read_text())
    backend=cfg.get('backend_url','http://leo-voice-backend.hermes-leo.svc.cluster.local:9120')
    try:
        if args.status: result=request(cfg,cfg['url'],'/status')
        elif args.check:
            result=request(cfg,backend,'/resolve',{'session_id':args.session_id or os.environ.get('HERMES_SESSION_ID')})
        elif args.tasks: result=request(cfg,backend,'/status')
        elif args.cancel: result=request(cfg,backend,'/cancel',{'call_id':str(uuid.UUID(args.cancel))})
        elif args.hangup: result=request(cfg,cfg['url'],'/hangup',{'call_id':str(uuid.UUID(args.hangup))})
        elif args.schedule_cancel: result=request(cfg,backend,'/schedule/cancel',{'event_id':args.schedule_cancel})
        elif args.calendar_preparation:
            result=request(cfg,backend,'/routines',{'calendar_preparation':args.calendar_preparation=='on'})
        elif args.routines:
            result=request(cfg,backend,'/routines',{'enabled':args.routines.lower()!='off','daily_review_time':'18:00' if args.routines.lower()=='off' else args.routines})
        else:
            if not 1<=len(args.reason)<=1000: parser.error('reason must contain 1–1000 characters')
            if args.kind in ('proactive','emergency') and not args.evidence.strip(): parser.error('verified evidence required')
            sid=args.session_id or os.environ.get('HERMES_SESSION_ID')
            origin=request(cfg,backend,'/resolve',{'session_id':sid})
            seed='leo-owner-phone:'+origin['session_id']+':'+origin['request_id']+':'+args.kind+':'+args.mode+':'+args.reason+':'+str(args.at)
            event=str(uuid.UUID(args.event_id)) if args.event_id else str(uuid.uuid5(uuid.NAMESPACE_URL,seed))
            body={'event_id':event,'reason':args.reason,'session_id':origin['session_id'],'mode':args.mode,
                  'kind':args.kind,'evidence':args.evidence}
            if args.deadline: body['deadline']=args.deadline
            if args.at:
                body.update(at=args.at,before_meeting=args.before_meeting)
                result=request(cfg,backend,'/schedule',body)
            else: result=request(cfg,cfg['url'],'/call',body)
        print(json.dumps(result,ensure_ascii=False))
    except urllib.error.HTTPError as exc:
        print(json.dumps({'http_status':exc.code,'detail':exc.read().decode()})); raise SystemExit(1)
    except (TimeoutError,urllib.error.URLError):
        print('Uncertain outcome. Check --status and --tasks before any retry.'); raise SystemExit(2)


if __name__=='__main__': main()
