from defined.constants import CAOS_DIR
from defined.post_init import GET_COMPILER

from clint.textui import puts, colored, indent
import os


def test(contest, task):
    task_path = os.path.join(CAOS_DIR, contest, task)
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

    if 'a.out' in os.listdir(os.getcwd()):
        os.remove('a.out')
    os.system(GET_COMPILER().format(os.path.join(task_path, 'main.c')))
    if 'a.out' not in os.listdir(os.getcwd()):
        puts(colored.red(f"Compilation error, aborted"))
        exit(0)

    for input in inputs:
        if input + '.ans' not in tests:
            puts(colored.yellow(f"No matching output for test {input}.dat. Skip it."))
            continue

        run_test(contest, task, input)

    os.remove('temp')
    os.remove('a.out')


def run_test(contest, task, test):
    task_path = os.path.join(CAOS_DIR, contest, task)
    input_path = os.path.join(task_path, 'tests', test + '.dat')
    output_path = os.path.join(task_path, 'tests', test + '.ans')

    os.system('./a.out < {} > temp'.format(input_path))

    with open(output_path, 'r') as output_file:
        with open('temp', 'r') as temp_file:
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
