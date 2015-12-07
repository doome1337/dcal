import datetime


def add_task(args):
    # time is currently converted to a datetime
    # so that alternate input methods can be made,
    # while output format remains the same.
    time = datetime.datetime.strptime(','.join([str(x) for x in args.time]),
                                      '%Y,%m,%d,%H,%M,%S')
    with open(args.cal_file, 'a') as calendar:
        calendar.write(
            args.task_name + "," +
            time.strftime('%Y,%m,%d,%H,%M,%S') + "," +
            args.status+'\n')
