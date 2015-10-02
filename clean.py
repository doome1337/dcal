import datetime

def clean(args):
    """Clean-up for planner files.

    Removes any tasks whose priority is above a certain amount.
    By default, it will remove tasks of status 2 or higher.

    @type file_name: str
    @type threshold: int
    @rtype: None

    >>> display('file.csv')
    Today is 2015-09-28 11:17:56.072809
    -----
    MAT157 Non-Standard Lecture... -- Incomplete. 02:06:42:03 left.
    MAT157 Non-Standard Lecture... -- Incomplete. 09:04:42:03 left.
    MAT157 Problem Set 2           -- To be revised. 00:03:42:03 left.
    asd                            -- Complete!
    asgsad                         -- Complete!
    >>> clean('file.csv')
    >>> display('file.csv')
    Today is 2015-09-28 11:17:56.074163
    -----
    MAT157 Non-Standard Lecture... -- Incomplete. 02:06:42:03 left.
    MAT157 Non-Standard Lecture... -- Incomplete. 09:04:42:03 left.
    MAT157 Problem Set 2           -- To be revised. 00:03:42:03 left.
    """
    file_name = args.cal_file
    task_code_file = args.format_file
    with open(file_name,'r') as calendar,open(task_code_file,'r') as code_file:
        lines = set(calendar.readlines())
        codes = map(lambda x: x.split(','),code_file.readlines())
        ots_remove = {}
        late_remove = {}
        remove = {}
        now_str = datetime.datetime.now().strftime('%Y,%m,%d,%H,%M,%S')
        for code in codes:
            ots_remove[code[0]] = bool(int(code[1]))
            late_remove[code[0]] = bool(int(code[2]))
        for line in lines:
            task_code = line.strip().split(',')[-1]
            remove[line] = ots_remove[task_code] or (late_remove[task_code] and
                    ','.join(line.split(',')[1:7]) < now_str)
    with open(file_name,'w') as calendar:
        for line in lines:
            if not remove[line]:
                calendar.write(line)

if __name__ == '__main__':
    #import sys
    #import os
    #__DEBUG__ = False
    #if __DEBUG__:
    #    import display
    #    display.display(sys.argv[1],sys.argv[2])
    #clean(sys.argv[1],sys.argv[2])
    #if __DEBUG__:
    #    display.display(sys.argv[1],sys.argv[2])
    pass
