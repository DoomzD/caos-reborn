from defined.post_init import ARGS_PATH, GET_COMPILER

from clint.textui import puts, colored, prompt

def set_gcc_args():
    puts(colored.yellow("right now compiler is:"))
    puts((f"{GET_COMPILER()[:-2]}"))
    puts(colored.yellow("new line of arguments for compiler (- to keep same, + to set default):"))
    args = prompt.query('gcc')

    if args == "-":
        exit(0)

    if args == "+":
        args = "-O2 -Wall -Werror -Wno-unused-result -std=gnu11 -lm -fsanitize=address -fsanitize=undefined -fno-sanitize-recover -fsanitize=leak"

    with open(ARGS_PATH, "w") as gcc_args:
        gcc_args.write(args)
