from clint.textui import puts, colored
import os

options = ['test', 'args', 'folder', 'help', 'gen']

def handler(mode, args):
    from .test import before_test
    from .modify import set_gcc_args, set_tasks_dir
    from .help import print_help
    from .generate import run_generator

    if mode == 'test':
        before_test(args)
    elif mode == 'gen':
        run_generator()
    elif mode == 'args':
        set_gcc_args()
    elif mode == 'folder':
        set_tasks_dir()
    elif mode == 'help':
        print_help()

    exit(0)
