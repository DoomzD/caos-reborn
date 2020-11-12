from defined.post_init import ARGS_PATH, GET_COMPILER, GET_CAOS_FOLDER, DIR_PATH
from defined.constants import gcc_string

from clint.textui import puts, colored, prompt

def set_gcc_args():
    puts(colored.yellow("right now compiler is:"))
    puts((f"{GET_COMPILER()[:-2]}"))
    puts(colored.yellow("new line of arguments for compiler (- to keep same, + to set default):"))
    ans = prompt.query('gcc')

    if ans == "-":
        exit(0)

    if ans == "+":
        ans = gcc_string

    #secret option
    if ans == "mac":
        ans = "-O2 -Wall -Werror -Wno-unused-result -std=gnu11 -lm -fsanitize=address -fsanitize=undefined -fno-sanitize-recover=all"

    with open(ARGS_PATH, "w") as gcc_args:
        gcc_args.write(ans)

def set_tasks_dir():
    tasks_dir_path = GET_CAOS_FOLDER()
    if tasks_dir_path == "-":
        puts(colored.red("folder is not chosen!"))
        puts(colored.yellow("folder to save tasks:"))
    else:
        puts(colored.yellow("right now tasks structure will be generated in:"))
        puts((f"{tasks_dir_path}"))
        puts(colored.yellow("new folder to save tasks(- to keep same):"))
    ans = prompt.query(">")

    if ans == "-":
        exit(0)

    with open(DIR_PATH, "w") as tasks_dir:
        tasks_dir.write(ans)
