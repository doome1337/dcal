def match(mode, case, task, given):
    if not case:
        task = task.lower()
        given = given.lower()
    if mode == 'equal':
        return task == given
    elif mode == 'start':
        return task.startswith(given)
    elif mode == 'in':
        return task.find(given) > -1


def update(args):
    with open(args.cal_file, 'r') as calendar:
        lines = calendar.readlines()
    with open(args.cal_file, 'w') as calendar:
        for line in lines:
            if not match(args.mode, args.case,
                         line.strip().split(',')[0], args.task_name):
                calendar.write(line)
            else:
                line_components = line.split(',')
                if args.time is None:
                    time = line_components[1:7]
                else:
                    time = [str(x) for x in args.time]
                if args.status is None:
                    status = line_components[7:]
                else:
                    status = [args.status+'\n']
                calendar.write(','.join(line_components[0:1]+time+status))
