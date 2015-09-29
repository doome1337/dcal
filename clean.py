def clean(file_name,threshold=2):
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
    with open(file_name,'r') as calendar:
        lines = calendar.readlines()
        remove = {}
        for line in lines:
            task_code = int(line.strip().split(',')[-1])
            remove[line] = (task_code>=threshold or task_code == -1)
    with open(file_name,'w') as calendar:
        calendar.write('task,y,m,d,h,m,s,status\n')
        for line in lines:
            if not remove[line]:
                calendar.write(line)

if __name__ == '__main__':
    import sys
    import os
    __DEBUG__ = False
    if __DEBUG__:
        import display
        display.display(sys.argv[1])
    clean(sys.argv[1])
    if __DEBUG__:
        display.display(sys.argv[1])
