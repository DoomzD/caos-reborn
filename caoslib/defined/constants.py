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

gcc_string = "-O2 -Wall -Werror -Wno-unused-result -std=gnu11 -lm -fsanitize=address -fsanitize=undefined -fno-sanitize-recover -fsanitize=leak"

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
