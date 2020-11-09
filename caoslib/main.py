from clint import arguments
from clint.textui import puts, colored

#this is far from ideal but a little more abstraction
if __name__ == '__main__':
    mode = arguments.Args()[0]
    flags = arguments.Args().flags

    #project init
    import initialization
    if mode in initialization.options:
        initialization.handler(mode, flags)

    #edjudje is needed
    import src
    if mode in src.options:
        src.handler(mode, flags)

    #just working with material on computer
    import tasks
    if mode in tasks.options:
        tasks.handler(mode, flags)

    puts(colored.red(f"No valid arguments are found"))
