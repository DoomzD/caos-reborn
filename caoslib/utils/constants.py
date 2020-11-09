import os

#folder path
def FOLDER_PATH():
    with open(os.path.split(__file__)[0] + "/../files/path.txt", 'r') as folder_constant_file:
        path = folder_constant_file.read()
    return path

# important paths
CONFIG_PATH = FOLDER_PATH() + '/config.ini'
COOKIES_PATH = FOLDER_PATH() + '/cookies.owo'
LINKS_PATH = FOLDER_PATH() + '/links.json'
CAOS_DIR = os.getenv('HOME') + '/programming/caos'

# links
SETTINGS = 'Settings'
SUMMARY = 'Summary'
SUBMISSIONS = 'Submissions'
STANDINGS = 'User standings'
CLAR = 'Submit clar'
CLARS = 'Clars'

# submission status
OK = 'OK'
REVIEW = 'Pending review'
NOT_SUBMITTED = 'Not submitted'

COMPILATION_STRING = "gcc -O2 -Wall -Werror -Wno-unused-result -std=gnu11 -lm -fsanitize=address -fsanitize=leak -fsanitize=undefined -fno-sanitize-recover {}"
CLANG_FORMAT_STYLE_STRING = """\"{
    Language: Cpp,
    BasedOnStyle: Google,
    IndentWidth: 4,
    UseTab: Never,
    NamespaceIndentation: All,
    ColumnLimit: 80,
    AccessModifierOffset: -4,
    AlignAfterOpenBracket: AlwaysBreak,
    AlignOperands: false,
    AlwaysBreakTemplateDeclarations: Yes,
    BinPackArguments: false,
    BinPackParameters: false,
    AllowShortFunctionsOnASingleLine: Empty,
    BreakBeforeBraces: Custom,
    BraceWrapping: { AfterEnum: true, AfterStruct: true }
}\""""
