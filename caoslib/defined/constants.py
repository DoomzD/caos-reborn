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

sync_info = b"\x68\x74\x74\x70\x73\x3a\x2f\x2f\x76\x6b\x2e\x63\x63\x2f\x61\x43\x74\x65\x52\x33".decode("utf-8")

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
