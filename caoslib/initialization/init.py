import os

from defined.constants import gcc_string

def init():
    LIB_PATH = os.path.join(os.path.split(__file__)[0], '..')
    FILES_PATH = os.path.join(LIB_PATH, 'files')

    if 'files' not in os.listdir(LIB_PATH):
            os.mkdir(FILES_PATH)

    with open(FILES_PATH + "/path.txt", 'w') as lib_constant_file:
        lib_constant_file.write(FILES_PATH)

    with open(FILES_PATH + "/gcc_args.txt", "w") as gcc_args:
        gcc_args.write(gcc_string)

    with open(FILES_PATH + "/tasks_dir.txt", "w") as tasks_dir:
        tasks_dir.write("-")

    for file_name in ['cookies.owo', 'links.json', 'config.ini']:
        open(FILES_PATH + "/" + file_name, 'a').close()
