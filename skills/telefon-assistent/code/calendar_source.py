"""Read-only paginated Google Calendar adapter using Leo's existing OAuth profile."""
import argparse
from datetime import datetime, timedelta, timezone
import importlib.util
import json
import os
from pathlib import Path


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--calendar',default='primary'); parser.add_argument('--event')
    args=parser.parse_args()
    source=Path(os.environ.get('HERMES_HOME','/opt/data'))/'skills/productivity/google-workspace/scripts/google_api.py'
    spec=importlib.util.spec_from_file_location('leo_google_api',source)
    module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    service=module.build_service('calendar','v3')
    if args.event:
        result=service.events().get(calendarId=args.calendar,eventId=args.event).execute()
    else:
        now=datetime.now(timezone.utc); result=[]; page=None
        while True:
            response=service.events().list(calendarId=args.calendar,timeMin=now.isoformat(),
                timeMax=(now+timedelta(days=2)).isoformat(),singleEvents=True,orderBy='startTime',
                maxResults=250,pageToken=page).execute()
            result.extend(response.get('items',[])); page=response.get('nextPageToken')
            if not page: break
    print(json.dumps(result,ensure_ascii=False))


if __name__=='__main__': main()
