import datetime
def add_task(args):
    #args.cal_file
    #args.task_name
    #args.time
    time = datetime.datetime.strptime(','.join(args.time),'%Y,%m,%d,%H,%M,%S')
    with open(args.cal_file,'a') as calendar:
        calendar.write(args.task_name+","+
                time.strftime('%Y,%m,%d,%H,%M,%S')+",inc")
