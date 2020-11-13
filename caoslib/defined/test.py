from defined.post_init import GET_COMPILER, GET_CAOS_FOLDER

from .modify import set_tasks_dir
from utils import c_file
from clint.textui import puts, colored, indent
import os


def test(contest, task):
    #not best solution cause have to add if everywhere and import in a lot of places, but i dont have a better idea withour ruining of order of iimport
    tasks_dir_path = GET_CAOS_FOLDER()
    if tasks_dir_path == "-":
        set_tasks_dir()
        tasks_dir_path = GET_CAOS_FOLDER()
    task_path = os.path.join(tasks_dir_path, contest, task)
    tests_path = os.path.join(task_path, 'tests')

    tests = []
    try:
        tests = os.listdir(tests_path)
    except:
        puts(colored.red(f"Path {tests_path} doesn't exist."))
        exit(0)

    inputs = filter(lambda x: x[x.find('.') + 1:] == 'dat', tests)
    inputs = list(map(lambda x: x[:x.find('.')], inputs))
    if not inputs:
        puts(colored.red(f"No tests found at {tests_path}"))
        exit(0)

    if 'a.out' in os.listdir(task_path):
        os.remove(f'{task_path}/a.out')

    c_file_name = c_file(os.listdir(task_path))
    os.system(GET_COMPILER().format(os.path.join(task_path, c_file_name.replace(" ", "\ ") )) + f" -o {task_path}/a.out")
    if 'a.out' not in os.listdir(task_path):
        puts(colored.red(f"Compilation error, aborted"))
        exit(0)

    for input in inputs:
        if input + '.ans' not in tests:
            puts(colored.yellow(f"No matching output for test {input}.dat. Skip it."))
            continue

        run_test(contest, task, input, task_path)

    os.remove(f'{task_path}/temp')
    os.remove(f'{task_path}/a.out')


def run_test(contest, task, test, task_path):
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
                find_diff(expected_lines, resulting_lines)
                exit(0)

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
