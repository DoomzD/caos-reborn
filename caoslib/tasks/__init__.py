from .test import test
from .style import style

options = ['test', 'style']

def handler(mode, flags):
    if mode == 'test':
        test(args)

    exit(0)
