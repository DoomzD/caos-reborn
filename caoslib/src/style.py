import utils.constants as const

from clint.textui import puts, colored, indent
import configparser
import os
import shutil


def style(args):
    config = configparser.ConfigParser()
    config['Tools'] = {}
    config.read(const.CONFIG_PATH)

    if '--set-tool' in args.grouped:
        config['Tools']['clang-format'] = args.grouped['--set-tool']
        with open(const.CONFIG_PATH, 'w') as configfile:
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
        for contest in os.listdir(const.CAOS_DIR):
            files += [
                os.path.join(const.CAOS_DIR, contest, task, 'main.c')
                for task in os.listdir(os.path.join(const.CAOS_DIR, contest))
            ]
    elif args.files:
        files = args.files

    command = (f"{tool}"
               "-style={const.CLANG_FORMAT_STYLE_STRING}"
               "--verbose -i"
               "{' '.join(str(file) for file in files)}")
    os.system(command)
