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
    days = days + d
    return "%02d:%02d:%02d:%02d" % (days, hours, minutes, seconds)

def task_format(task):
    """Formats a task name to appear correctly.

    If shorter than 30 characters,
    it is padded with spaces.
    If longer, it cuts it down to 27 characters,
    and adds an ellipsis.

    @type time: str
    @rtype str

    >>> task_format('Hello World!')
    'Hello World!                  '
    >>> task_format("This line is 30 characters, yo")
    'This line is 30 characters, yo'
    >>> task_format("This line is way too long to fit normally.")
    'This line is way too long t...'
    """
    length = len(task)
    # Together with the double dash,
    # this makes 32 characters before the status.
    if length > 30:
        return task[0:27] + "..."
    else:
        return task + (" "*(30-length))

def display(file_name):
    now = datetime.datetime.now()
    events = []
    print ("")
    print ("Today is " + str(now))
    print ("-----")
    with open(file_name,"r") as calendar:
        lines = calendar.readlines()[1:]
        for line in lines:
            data = line.split(",")
            due_date = datetime.datetime(int(data[1]),\
                    int(data[2]),int(data[3]),int(data[4]),\
                    int(data[5]),int(data[6]))
            until = due_date - now
            events.append([data[0],int(data[7]),until])
    for i in range(len(events)):
        for j in range(i,len(events)):
            if (events[i][1] > events[j][1]) or \
                    (events[i][2] > events[j][2] and \
                    not events[i][1] < events[j][1]):
                temp = events[i]
                events[i] = events[j]
                events[j] = temp
    # A list of Completion Codes:
    # 0: Incomplete
    # 1: Complete, but needs revision/submission
    # 2: Completed, submitted.
    for i in events:
        if i[1] == 0:
            if i[2] > datetime.timedelta(0):
                print (task_format(i[0]) + ' -- Incomplete. ' \
                        + time_format(i[2]) + " left.")
            else:
                print (task_format(i[0]) + ' -- OVERDUE! ' \
                        + time_format(-i[2]) + " late!")
        elif i[1] == 1:
            if i[2] > datetime.timedelta(0):
                print (task_format(i[0]) + ' -- To be revised. ' \
                        + time_format(i[2]) + " left.")
            else:
                print (task_format(i[0]) + ' -- OVERDUE! ' \
                        + time_format(-i[2]) + " late!")
        else:
            print (task_format(i[0]) + ' -- Complete!')
    print ("")

if __name__ == '__main__':
    display(sys.argv[1])
