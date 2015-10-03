def match(mode,case,task,given):
    if not case:
        task = task.lower()
        given = given.lower()
    if mode == 'equal':
        return task == given
    elif mode == 'start':
        return task.startswith(given)
    elif mode == 'in':
        return task.find(given)>-1


def remove(args):
    with open(args.cal_file,'r') as calendar:
        lines = calendar.readlines()
    with open(args.cal_file,'w') as calendar:
        for line in lines:
            if not match(args.mode,args.case,
                    line.split(',')[0],args.task_name):
                calendar.write(line)
