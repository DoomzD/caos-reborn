from .init import init
from clint.textui import puts, colored

options = ['init']

def handler(mode, flags):
    init()
    puts(colored.green("Init successful"))

    exit(0)
