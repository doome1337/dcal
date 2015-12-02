import datetime


def date_gen(event):
    now = datetime.datetime.now().strftime("%Y,%U,%w,%H,%M,%S").split(',')
    # event_format = 'Name,%w,%H,M,%S'
    if event[1:] < now[-4:]:
        event_date = [now[0]]+[str(int(now[1])+1)]+event[1:]
    else:
        event_date = now[0:2]+event[1:]
    event_dt = (datetime.datetime.strptime(','.join(event_date),
                                           '%Y,%U,%w,%H,%M,%S')
                .strftime('%Y,%m,%d,%H,%M,%S'))
    return event[0]+','+event_dt+',rec\n'


def gen_events(args):
    gen_file = args.source_file
    event_file = args.cal_file
    open(gen_file, "a").close()
    with open(gen_file, 'r') as schedule, open(event_file, 'a') as calendar:
        events = schedule.readlines()
        for event in events:
            calendar.write(date_gen(event.strip().split(',')))
