import datetime
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
for i in events:
    if i[1] == 0:
        if i[2] > datetime.timedelta(0):
            print i[0] + " on time. " + str(i[2]) + " left."
        else:
            print i[0] + " OVERDUE! " + str(-i[2]) + " late!"
    else:
        print i[0] + " Complete!"
print 
