import sys
import os

def clean(file_name,threshold):
    with open(file_name,'r') as calendar:
        lines = calendar.readlines()[1:]
        remove = {}
        for line in lines:
            remove[line]=int(line.strip().split(',')[-1])>=threshold
    with open(file_name,'w') as calendar:
        calendar.write('task,y,m,d,h,m,s,status\n')
        for line in lines:
            if not remove[line]:
                calendar.write(line)

if __name__ == '__main__':
    __DEBUG__ = False
    if __DEBUG__:
        import display
        display.display(sys.argv[1])
    clean(sys.argv[1],2)
    if __DEBUG__:
        display.display(sys.argv[1])
