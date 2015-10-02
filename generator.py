import datetime
import os
import sys

def date_gen(event):
    now = datetime.datetime.now().strftime("%Y,%U,%w,%H,%M,%S").split(',')
    #event_format = 'Name,%w,%H,M,%S'
    if event[1:] < now[-4:]:
        event_date = [now[0]]+[str(int(now[1])+1)]+event[1:]
    else:
        event_date = now[0:2]+event[1:]
    event_dt = (datetime.datetime.strptime(','.join(event_date),'%Y,%U,%w,%H,%M,%S')
            .strftime('%Y,%m,%d,%H,%M,%S'))
    return event[0]+','+event_dt+',rec\n'

def gen_events(gen_file,event_file):
    with open(gen_file,'r') as schedule, open(event_file,'a') as calendar:
        events = schedule.readlines()
        for event in events:
            calendar.write(date_gen(event.strip().split(',')))

if __name__ == '__main__':
    gen_events(sys.argv[1],sys.argv[2])
