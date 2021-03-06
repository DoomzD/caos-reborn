from defined.post_init import GET_COMPILER, GET_CAOS_FOLDER

from .modify import set_tasks_dir
from utils import c_file
from clint.textui import puts, colored, indent
import os

abort_text = colored.red("Start with a folder with .c file and tests folder or provide both -c and -t flags for testing")

def before_test(args):
    grouped = args.grouped

    debug_mode = []
    if '-d' in grouped:
        if len(grouped['-d']) == 0:
            debug_mode = ['000']
        else:
            debug_mode = grouped['-d'].all

    if '-c' not in grouped or '-t' not in grouped or len(grouped['-c']) == 0 or len(grouped['-t']) == 0:
        task_path = os.getcwd()
    else:
        #not best solution cause have to add if everywhere and import in a lot of places, but i dont have a better idea withour ruining of order of iimport
        tasks_dir_path = GET_CAOS_FOLDER()
        if tasks_dir_path == "-":
            set_tasks_dir()
            tasks_dir_path = GET_CAOS_FOLDER()
        task_path = os.path.join(tasks_dir_path, grouped['-c'][0], grouped['-t'][0])

    tests_path = os.path.join(task_path, 'tests')
    c_file_name = c_file(os.listdir(task_path))

    if not(c_file_name):
        puts(colored.red(f"No .c file found in {task_path}. ") + abort_text)
        exit(0)

    if not(os.path.exists(tests_path)):
        puts(colored.red(f"Path {tests_path} doesn't exist. ") + abort_text)
        exit(0)

    test(task_path, tests_path, c_file_name, debug_mode)

def test(task_path, tests_path, c_file_name, debug_vals = []):

    tests = os.listdir(tests_path)

    if len(debug_vals) > 0:
        inputs = debug_vals
    else:
        inputs = filter(lambda x: x[x.find('.') + 1:] == 'dat', tests)
        inputs = list(map(lambda x: x[:x.find('.')], inputs))

    if not inputs:
        puts(colored.red(f"No tests found at {tests_path}"))
        exit(0)

    if 'a.out' in os.listdir(task_path):
        os.remove(f'{task_path}/a.out')



    os.system(GET_COMPILER().format(os.path.join(task_path, c_file_name.replace(" ", "\ ") )) + f" -o {task_path}/a.out")
    if 'a.out' not in os.listdir(task_path):
        puts(colored.red(f"Compilation error, aborted"))
        exit(0)

    for input in inputs:
        if input + '.ans' not in tests:
            puts(colored.yellow(f"No matching output for test {input}.dat. Skip it."))
            continue

        run_test(input, task_path, len(debug_vals) > 0)

    os.remove(f'{task_path}/temp')
    os.remove(f'{task_path}/a.out')


def run_test(test, task_path, debug_mode):
    input_path = os.path.join(task_path, 'tests', test + '.dat')
    output_path = os.path.join(task_path, 'tests', test + '.ans')

    os.system(f'{task_path}/a.out < {input_path} > {task_path}/temp'.format())

    with open(output_path, 'r') as output_file:
        with open(f'{task_path}/temp', 'r') as temp_file:
            expected_lines = output_file.readlines()
            resulting_lines = temp_file.readlines()

            if expected_lines == resulting_lines:
                puts(colored.green(f"Test {test}: OK!"))
            else:
                puts(colored.red(f"Test {test}: Failed!"))
                if not(debug_mode):
                    find_diff(expected_lines, resulting_lines)
                    exit(0)
                else:
                    puts(colored.yellow("Expected:"))
                    for line in expected_lines:
                        print(line, end = "")
                    puts(colored.yellow("Got output:"))
                    for line in resulting_lines:
                        print(line, end = "")

def find_diff(expected_lines, resulting_lines):
    count = 0
    for (line, (expected, resulting)) in enumerate(zip(expected_lines, resulting_lines)):
        if expected != resulting:
            with indent(quote=f'  Line #{line + 1} > '):
                puts(colored.blue(f"Expected:  {expected}"), newline=False)
                puts(colored.yellow(f"Resulting: {resulting}"))
            count += 1

        if count == 10:
            break

    puts(colored.red(f"Resulting output saved to the 'temp' file."))
