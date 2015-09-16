import datetime

def time_format(time):
    s = time.seconds
    d = time.days
    minutes, seconds = divmod(s, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    days = days + d
    return "%02d:%02d:%02d:%02d" % (days, hours, minutes, seconds)

def task_format(task):
    length = len(task)
    # Together with the quotes and the space, 
    # this makes 32 characters before the status.
    if length > 29:
        return task[0:26] + "..."
    else:
        return task + (" "*(29-length))

now = datetime.datetime.now()
events = []
print
print "Today is " + str(now)
print "-----"
with file("planner.csv","r") as calendar:
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
            print '"' + task_format(i[0]) + '" incomplete. ' \
                    + time_format(i[2]) + " left."
        else:
            print '"' + task_format(i[0]) + '" OVERDUE! ' \
                    + time_format(-i[2]) + " late!"
    elif i[1] == 1:
        if i[2] > datetime.timedelta(0):
            print '"' + task_format(i[0]) + '" complete, but unfinished. ' \
                    + time_format(i[2]) + " left."
        else:
            print '"' + task_format(i[0]) + '" OVERDUE! ' \
                    + time_format(-i[2]) + " late!"
    else:
        print '"' + task_format(i[0]) + '" complete!'
print 
