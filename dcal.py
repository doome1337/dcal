#!/usr/bin/env python3.4
# This is here since I don't want dcal.py imported.
# This is the main file. 
# It shouldn't do anything when it isn't main.
if __name__ == '__main__':
    # Import other files in dcal.
    # Maybe I should clean this up.
    # Although having one file would be a bit messy...
    import display
    import clean
    import generator
    import addtask
    import init
    import remove
    import update

    # Import modules no in dcal.
    import argparse
    from os.path import expanduser
    home = expanduser("~")
    cal_file = home+'/.dcal'
    gen_file = home+'/.dcalgen'
    code_file = home+'/.dcalcode'
    parser = argparse.ArgumentParser(description='Calendar Utility')
    subparsers = parser.add_subparsers()
    display_parser = subparsers.add_parser('display',aliases=['dis'])
    display_parser.add_argument('--cal_file',type=str,default=cal_file,
            help='calendar file to display.')
    display_parser.add_argument('--format_file',type=str,default=code_file)
    display_parser.add_argument('-p','--priority',nargs='?',
            type=int,default=0,const=10,
            help='Display only tasks with a certain priority. '+
            'Currently, priority is determined by task type.')
    display_parser.set_defaults(func=display.display)
    clean_parser = subparsers.add_parser('clean')
    clean_parser.add_argument('--cal_file',type=str,default=cal_file,
            help='calendar file to clean.')
    clean_parser.add_argument('--format_file',type=str,default=code_file,
            help='format file containing all event types.')
    clean_parser.set_defaults(func=clean.clean)
    gen_parser = subparsers.add_parser('generate',aliases=['gen'])
    gen_parser.add_argument('--source_file',type=str,default=gen_file,
            help='source file from which the recurring events are loaded.')
    gen_parser.add_argument('--cal_file',type=str,default=cal_file,
            help='calendar file to which to write the recurring tasks.')
    gen_parser.set_defaults(func=generator.gen_events)
    addtask_parser = subparsers.add_parser('add')
    addtask_parser.add_argument('task_name',type=str,
            help='name of event or task to complete.')
    addtask_parser.add_argument('time',nargs=6,type=int,
            help='time of event in the form YYYY MM DD HH MM SS.')
    addtask_parser.add_argument('--cal_file',type=str,default=cal_file,
            help='calendar file to which to write the task.')
    addtask_parser.add_argument('-s','--status',nargs='?',default='inc',
            type=str,help='status of task to append.')
    addtask_parser.set_defaults(func=addtask.add_task)
    """init_parser = subparsers.add_parser('initialize',aliases=['init'],
            description='Initialize all necessary files to their defaults.')
    init_parser.add_argument('-f',"--files",nargs=3,
            default=[cal_file,gen_file,code_file],
            help='which folder to initialize the files in. '+
            'The order is cal_file, gen_file, code_file.')
    init_parser.set_defaults(func=init.init)"""
    rem_parser = subparsers.add_parser('remove',aliases=['rem'])
    rem_parser.add_argument('task_name',type=str,
            help='name of event or task to remove')
    rem_parser.add_argument('--cal_file',type=str,default=cal_file,
            help='calendar file from which to remove the task.')
    rem_case = rem_parser.add_mutually_exclusive_group()
    rem_case.add_argument('-c','--case',action='store_const',
            const=True,dest='case',
            help='Enable case-sensitivity.')
    rem_case.add_argument('-I','--icase',action='store_const',
            const=False,dest='case',
            help='Enable case-insensitivity. This is the default')
    rem_mode = rem_parser.add_mutually_exclusive_group()
    rem_mode.add_argument('-s','--startswith',action='store_const',
            const='start',dest='mode',
            help='Remove any tasks that start with the given string.')
    rem_mode.add_argument('-e','--equals',action='store_const',
            const='equal',dest='mode',
            help='Remove any tasks that exactly match the given string. '+
            'This is the default mode.')
    rem_mode.add_argument('-i','--in',action='store_const',
            const='in',dest='mode',
            help='Remove any tasks that contain the given string.')
    rem_parser.set_defaults(func=remove.remove,mode='equal',case=False)
    update_parser = subparsers.add_parser('update',aliases=['upd'])
    update_parser.add_argument('task_name',type=str,
            help='name of even or task to update.')
    update_parser.add_argument('--cal_file',type=str,default=cal_file,
            help='calendar file to update.')
    update_parser.add_argument('-t','--time',nargs=6,type=int,
            help='Update the time.')
    update_parser.add_argument('-S','--status',type=str,
            help='Update the status.')
    update_case = update_parser.add_mutually_exclusive_group()
    update_case.add_argument('-c','--case',action='store_const',
            const=True,dest='case',
            help='Enable case-sensitivity.')
    update_case.add_argument('-I','--icase',action='store_const',
            const=False,dest='case',
            help='Enable case-insensitivity. This is the default')
    update_mode = update_parser.add_mutually_exclusive_group()
    update_mode.add_argument('-s','--startswith',action='store_const',
            const='start',dest='mode',
            help='Update any tasks that start with the given string.')
    update_mode.add_argument('-e','--equals',action='store_const',
            const='equal',dest='mode',
            help='Update any tasks that exactly match the given string. '+
            'This is the default mode.')
    update_mode.add_argument('-i','--in',action='store_const',
            const='in',dest='mode',
            help='Update any tasks that contain the given string.')
    update_parser.set_defaults(func=update.update,mode='equa',case=False)
    args = parser.parse_args()
    args.func(args)
