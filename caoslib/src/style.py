from defined.post_init import CONFIG_PATH
from defined.constants import CAOS_DIR, CLANG_FORMAT_STYLE_STRING

import configparser
import os
import shutil
from clint.textui import puts, colored, indent


def style(args):
    config = configparser.ConfigParser()
    config['Tools'] = {}
    config.read(CONFIG_PATH)
    #no idea how this works
    if '--set-tool' in args.grouped:
        config['Tools']['clang-format'] = args.grouped['--set-tool']
        with open(CONFIG_PATH, 'w') as configfile:
            config.write(configfile)

        puts(colored.green('clang-format tool path changed succesfully!'))
        exit(0)

    tool = args.grouped.get(
        '-t', config['Tools'].get('clang-format',
                                  shutil.which('clang-format')))

    if not tool or not os.path.exists(tool):
        puts(
            colored.red(
                "clang-format is not found in $PATH and not specified explicitly."
                "Try modifying $PATH, or use one of '--set-tool' and '-t' flags."
            ))
        exit(1)

    files = []
    if '--all' in args.flags:
        for contest in os.listdir(CAOS_DIR):
            files += [
                os.path.join(CAOS_DIR, contest, task, 'main.c')
                for task in os.listdir(os.path.join(CAOS_DIR, contest))
            ]
    elif args.files:
        files = args.files

    command = (f"{tool}"
               f"-style={CLANG_FORMAT_STYLE_STRING}"
               "--verbose -i"
               f"{' '.join(str(file) for file in files)}")
    os.system(command)
