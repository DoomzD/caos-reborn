from defined.post_init import ARGS_PATH

import os

def init():
    LIB_PATH = os.path.join(os.path.split(__file__)[0], '..')
    FILES_PATH = os.path.join(LIB_PATH, 'files')

    if 'files' not in os.listdir(LIB_PATH):
            os.mkdir(FILES_PATH)

    with open(LIB_PATH + "/../caos", 'w') as bash:
        bash.write(f'python3 {LIB_PATH}/main.py "$@"')

    with open(FILES_PATH + "/path.txt", 'w') as lib_constant_file:
        lib_constant_file.write(FILES_PATH)

    with open(FILES_PATH + "/gcc_args.txt", "w") as gcc_args:
        gcc_args.write("-O2 -Wall -Werror -Wno-unused-result -std=gnu11 -lm -fsanitize=address -fsanitize=undefined -fno-sanitize-recover -fsanitize=leak")

    for file_name in ['cookies.owo', 'links.json', 'config.ini']:
        open(FILES_PATH + "/" + file_name, 'a').close()

def set_gcc_args(args):
    with open(ARGS_PATH, "w") as gcc_args:
        gcc_args.write(args)
