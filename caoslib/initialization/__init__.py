from .init import init
from clint.textui import puts, colored

options = ['init']

def handler(mode):
    init()
    puts(colored.green("Init successful"))

    exit(0)
