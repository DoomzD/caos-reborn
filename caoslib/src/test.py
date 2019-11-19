from utils.constants import CAOS_DIR, COMPILATION_STRING

from clint.textui import puts, colored, indent
import os, pathlib


def test(args):
    (contest, task) = get_task_name(args)
    tests_path = os.path.join(CAOS_DIR, contest, task, 'tests');

    tests = []
    try:
        tests = os.listdir(tests_path)
    except:
        puts(colored.red(f"Path {tests_path} doesn't exist."))
        exit(0)

    inputs = filter(lambda x: x[x.find('.') + 1:] == 'dat', tests)
    inputs = map(lambda x: x[:x.find('.')], inputs)

    for input in inputs:
        if input + '.ans' not in tests:
            puts(colored.yellow(f"No matching output for test {input}.dat. Skip it."))
            continue

        run_test(contest, task, input)


def get_task_name(args):
    grouped = args.grouped
    if '-c' not in grouped or '-t' not in grouped or len(grouped['-c']) == 0 or len(grouped['-t']) == 0:
        puts(colored.red("Provide both -c and -t flags for testing."))
        exit(0)
    return (grouped['-c'][0], grouped['-t'][0])


def run_test(contest, task, test):
    task_path = os.path.join(CAOS_DIR, contest, task)
    input_path = os.path.join(task_path, 'tests', test + '.dat')
    output_path = os.path.join(task_path, 'tests', test + '.ans')

    os.system(COMPILATION_STRING.format(task_path + '/main.c'))
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

    os.remove('temp')
    os.remove('a.out')


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
