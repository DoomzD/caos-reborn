from clint.textui import puts, colored

options = ['test', 'args']

def handler(mode, args):
    from .test import test
    from .modify import set_gcc_args

    if mode == 'test':
        grouped = args.grouped
        if '-c' not in grouped or '-t' not in grouped or len(grouped['-c']) == 0 or len(grouped['-t']) == 0:
            puts(colored.red("Provide both -c and -t flags for testing."))
            exit(0)
        test(grouped['-c'][0], grouped['-t'][0])
    elif mode == 'args':
        set_gcc_args()
    exit(0)
