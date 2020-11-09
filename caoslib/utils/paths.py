import os

#lib path
def LIB_PATH():
    with open(os.path.split(__file__)[0] + "/../files/path.txt", 'r') as folder_constant_file:
        path = folder_constant_file.read()
    return path


#relative to lib paths
CONFIG_PATH = LIB_PATH() + '/config.ini'
COOKIES_PATH = LIB_PATH() + '/cookies.owo'
LINKS_PATH = LIB_PATH() + '/links.json'
