def init(args):
    for file in args.files:
        with open(file, 'a+') as f:
            f.write('')
