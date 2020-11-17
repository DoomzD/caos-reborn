from clint.textui import puts, colored

def print_help():
        puts(colored.yellow("general commands"))
        puts("init\t: reboot the settings of project and setup everything")
        puts("help\t: this info")
        puts("args\t: change args for gcc compiler")
        puts("folder\t: change folder with tasks")

        puts(colored.yellow("ejudge commands"))
        puts("login\t: saves login and password for caos.ejudge.ru")
        puts("info\t: outputs standings info")
        puts("status\t: your tasks status after you send them")
        puts("\t\t -s show only ok/pending review \t\t *optional")

        puts(colored.yellow("tasks commands"))
        puts("test\t: tests program on your local tests")
        puts("\t\t -c contest name \t\t *required")
        puts("\t\t -t task number \t\t *required")
        puts("style\t: changes your local tasks style")
        puts("\t\t --all if you want to clang-style all your local files \t *optional")
        puts("\t\t -c contest name \t\t *required")
        puts("\t\t -t task number \t\t *required")
        puts("sync\t: creates folders for your tasks in a local folder")
        puts("\t\t -ssa, --sync-samples also download first test \t\t *optional")
        puts("\t\t -sst, --sync-statements also download statements\t *optional")
        puts("\t\t -sa, --sync-all combination of previous options\t *optional")
