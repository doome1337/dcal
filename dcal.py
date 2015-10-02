#!/usr/bin/env python3.4
# This is here since I don't want dcal.py imported.
# This is the main file. 
# It shouldn't do anything when it isn't main.
if __name__ == '__main__':
    import display
    import clean
    import generator
    import argparse
    parser = argparse.ArgumentParser(description='Calendar Utility')
    subparsers = parser.add_subparsers(metavar="display,clean,generate")
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
    args = parser.parse_args()
    args.func(args)
