from defined.post_init import CONFIG_PATH, GET_CAOS_FOLDER, FORMAT_PATH
from defined.constants import CLANG_FORMAT_STYLE_STRING
from offline.modify import set_tasks_dir
from utils import c_file

import configparser
import os
import shutil
from clint.textui import puts, colored, indent


def style(args):
    tasks_dir_path = GET_CAOS_FOLDER()
    if tasks_dir_path == "-":
        set_tasks_dir()
        tasks_dir_path = GET_CAOS_FOLDER()

    grouped = args.grouped
    if ('-c' not in grouped or '-t' not in grouped or len(grouped['-c']) == 0 or len(grouped['-t']) == 0) and (not '--all' in args.flags):
        puts(colored.red("Provide both -c and -t flags for formating or choose --all"))
        exit(0)

    #this is just getting clang-format bin and sending files there....
    """
    config = configparser.ConfigParser()
    config['Tools'] = {}
    config.read(CONFIG_PATH)
    if '--set-tool' in args.grouped:
        config['Tools']['clang-format'] = args.grouped['--set-tool']
        with open(CONFIG_PATH, 'w') as configfile:
            config.write(configfile)

        puts(colored.green('clang-format tool path changed succesfully!'))
        exit(0)

    tool = args.grouped.get(
        '-format', config['Tools'].get('clang-format',
                                  shutil.which('clang-format')))

    if not tool or not os.path.exists(tool):
        puts(
            colored.red(
                "clang-format is not found in $PATH and not specified explicitly."
                "Try modifying $PATH, or use one of '--set-tool' and '-t' flags."
            ))
        exit(1)
    """
    tool = FORMAT_PATH

    files = []
    if '--all' in args.flags:
        for contest in os.listdir(tasks_dir_path):
            for task in os.listdir(os.path.join(tasks_dir_path, contest)):
                task_path = os.path.join(tasks_dir_path, contest, task)
                c_file_name = c_file(os.listdir(task_path))
                files.append(os.path.join(task_path, c_file_name.replace(" ", "\ ")))
    else:
        contest = grouped['-c'][0]
        task = grouped['-t'][0]
        task_path = os.path.join(tasks_dir_path, contest, task)
        c_file_name = c_file(os.listdir(task_path))
        files.append(os.path.join(task_path, c_file_name.replace(" ", "\ ")))

    command = (f"{tool} "
               f"-style={CLANG_FORMAT_STYLE_STRING} "
               "--verbose -i "
               f"{' '.join(str(file) for file in files)}")
    os.system(command)
