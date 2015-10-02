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
    display_parser.add_argument('cal_file')
    display_parser.add_argument('format_file')
    display_parser.set_defaults(func=display.display)
    clean_parser = subparsers.add_parser('clean')
    clean_parser.add_argument('cal_file')
    clean_parser.add_argument('format_file')
    clean_parser.set_defaults(func=clean.clean)
    gen_parser = subparsers.add_parser('generate',aliases=['gen'])
    gen_parser.add_argument('source_file')
    gen_parser.add_argument('cal_file')
    gen_parser.set_defaults(func=generator.gen_events)
    addtask_parser = subparsers.add_parser('add')
    addtask_parser.add_argument('cal_file')
    addtask_parser.add_argument('task_name')
    addtask_parser.add_argument('time',nargs=6)
    addtask_parser.set_defaults(func=addtask.add_task)
    args = parser.parse_args()
    args.func(args)
