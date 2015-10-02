import datetime
import sys

def time_format(time):
    """Formats a timedelta in the form DD:HH:MM:SS.

    @type time: timedelta
    @rtype str

    >>> time_format(datetime.timedelta(hours=10))
    '00:10:00:00'
    >>> time_format(datetime.timedelta(hours=25))
    '01:01:00:00'
    >>> time_format(datetime.timedelta(hours=4,seconds=15,minutes=26,days=7))
    '07:04:26:15'
    """
    s = time.seconds
    d = time.days
    minutes, seconds = divmod(s, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    days += d
    return "%02d:%02d:%02d:%02d" % (days, hours, minutes, seconds)

def task_format(task,code):
    length = len(task[0])
    if length > 30:
        namestr = task[0][0:27] + "..."
    else:
        namestr = task[0] + (" "*(30-length))
    curstr = namestr.join(code.split('%N'))
    timestr = time_format(task[2])
    curstr = timestr.join(curstr.split('%T'))
    atimestr = task[3].isoformat(',')
    return atimestr.join(curstr.split('%A'))

def display(file_name, task_codes_file):
    now = datetime.datetime.now()
    events = []
    priorities = {}
    print ("")
    print ("Today is " + str(now))
    print ("-----")
    with open(file_name,"r") as calendar, \
        open(task_codes_file,'r') as task_codes:
        lines = map(lambda x:x.strip().split(','),calendar.readlines())
        codes = map(lambda x:x.strip().split(','),task_codes.readlines())
        for code in codes:
            priorities[code[0]]=int(code[3])
        for line in lines:
            due_date = datetime.datetime(int(line[1]),
                    int(line[2]),int(line[3]),int(line[4]),
                    int(line[5]),int(line[6]))
            until = due_date - now
            events.append([line[0],line[7],until,due_date])
    for i in range(len(events)):
        for j in range(i,len(events)):
            if (priorities[events[i][1]] < priorities[events[j][1]]) or \
                    (events[i][2] > events[j][2] and \
                    not priorities[events[i][1]] > priorities[events[j][1]]):
                events[i],events[j] = events[j],events[i]
    for event in events:
        for code in codes:
            if event[1] == code[0]:
                if event[2] > datetime.timedelta(0):
                    print task_format(event,code[4])
                else:
                    print task_format(event[0:2]+[-event[2]]+event[3:],code[5])
    print ("")

if __name__ == '__main__':
    display(sys.argv[1], sys.argv[2])
