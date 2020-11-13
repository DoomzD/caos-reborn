from clint import arguments
from clint.textui import puts, colored

#i am thinking of removing puts/prompt.query for print/input
#this is far from ideal but a little more abstraction
if __name__ == '__main__':
    mode = arguments.Args()[0]
    args = arguments.Args()

    #project init
    import initialization
    if mode in initialization.options:
        initialization.handler(mode, args)

    #edjudje is needed
    import src
    if mode in src.options:
        src.handler(mode, args)

    #just working with material on computer
    import offline
    if mode in offline.options:
        offline.handler(mode, args)

    puts(colored.red(f"No valid arguments were found"))
