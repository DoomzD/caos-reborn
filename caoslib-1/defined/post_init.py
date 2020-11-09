import os

#lib path
def FILES_PATH():
    with open(os.path.split(__file__)[0] + "/../files/path.txt", 'r') as folder_constant_file:
        path = folder_constant_file.read()
    return path

def GET_COMPILER():
    with open(ARGS_PATH, "r") as gcc_args:
        return "gcc " + gcc_args.read() + " {}"


#relative to lib paths
CONFIG_PATH = FILES_PATH() + '/config.ini'
COOKIES_PATH = FILES_PATH() + '/cookies.owo'
LINKS_PATH = FILES_PATH() + '/links.json'
ARGS_PATH = FILES_PATH() + '/gcc_args.txt'
