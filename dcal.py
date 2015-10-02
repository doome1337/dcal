#!/usr/bin/env python3.4
# This is here since I don't want dcal.py imported.
# This is the main file. 
# It shouldn't do anything when it isn't main.
if __name__ == '__main__':
    import display
    import clean
    import generator
    import addtask
    import argparse
    parser = argparse.ArgumentParser(description='Calendar Utility')
    subparsers = parser.add_subparsers()
    display_parser = subparsers.add_parser('display',aliases=['dis'])
    display_parser.add_argument('cal_file',type=str,
            help='calendar file to display.')
    display_parser.add_argument('format_file')
    display_parser.set_defaults(func=display.display)
    clean_parser = subparsers.add_parser('clean')
    clean_parser.add_argument('cal_file',type=str,
            help='calendar file to clean.')
    clean_parser.add_argument('format_file',type=str,
            help='format file containing all event types.')
    clean_parser.set_defaults(func=clean.clean)
    gen_parser = subparsers.add_parser('generate',aliases=['gen'])
    gen_parser.add_argument('source_file',type=str,
            help='source file from which the recurring events are loaded.')
    gen_parser.add_argument('cal_file',type=str,
            help='calendar file to which to write the recurring tasks.')
    gen_parser.set_defaults(func=generator.gen_events)
    addtask_parser = subparsers.add_parser('add')
    addtask_parser.add_argument('cal_file',type=str,
            help='calendar file to which to write the task.')
    addtask_parser.add_argument('task_name',type=str,
            help='name of event or task to complete.')
    addtask_parser.add_argument('time',nargs=6,type=int,
            help='time of event in the form YYYY MM DD HH MM SS.')
    addtask_parser.add_argument('-s','--status',nargs='?',default='inc',
            type=str,help='status of task to append.')
    addtask_parser.set_defaults(func=addtask.add_task)
    args = parser.parse_args()
    args.func(args)
