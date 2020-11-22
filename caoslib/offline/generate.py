import os
from clint.textui import puts, colored

def run_generator():

    generator = os.path.join(os.getcwd(), "gen.py")
    if not(os.path.isfile(generator)):
        puts(colored.red("start with a gen.py in your folder"))
        exit(0)
    os.system("python3 gen.py")
