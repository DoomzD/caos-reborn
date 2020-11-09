import os

def init():
    LIB_PATH = os.path.join(os.getcwd(), 'caoslib', 'files')
    if 'files' not in os.listdir(os.getcwd() + '/caoslib'):
            os.mkdir(LIB_PATH)

    with open(os.getcwd() + "/caos", 'w') as bash:
        bash.write(f'python3 {os.getcwd()}/caoslib/main.py "$@"')

    with open(LIB_PATH + "/path.txt", 'w') as lib_constant_file:
        lib_constant_file.write(LIB_PATH)

    for file_name in ['cookies.owo', '/links.json', '/config.ini']:
        open(LIB_PATH + "/" + file_name, 'a').close()
