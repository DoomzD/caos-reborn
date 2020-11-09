from clint.textui import puts, colored, indent

options = ['test', 'style']

def handler(mode, args):
    from .test import test
    if mode == 'test':
        (contest, task) = get_task_name(args)
        test(contest, task)
    exit(0)

def get_task_name(args):
    grouped = args.grouped
    if '-c' not in grouped or '-t' not in grouped or len(grouped['-c']) == 0 or len(grouped['-t']) == 0:
        puts(colored.red("Provide both -c and -t flags for testing."))
        exit(0)
    return (grouped['-c'][0], grouped['-t'][0])
