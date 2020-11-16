from defined.post_init import GET_CAOS_FOLDER
from defined.generator import generator_text
from defined.constants import sync_info
from offline.modify import set_tasks_dir
from utils import get_problems, c_file

import os
from bs4 import BeautifulSoup as bs
from clint.textui import puts


def sync(session, sync_samples, sync_statements, sync_other, target_contest='all', extension='.c'):
    if sync_other:
        puts(sync_info)
        exit(0)
    tasks_dir_path = GET_CAOS_FOLDER()
    if tasks_dir_path == "-":
        set_tasks_dir()
        tasks_dir_path = GET_CAOS_FOLDER()

    files = os.listdir(tasks_dir_path)
    problems = get_problems(session)

    for problem in problems:
        short_name = problem['short name']
        contest = short_name[:short_name.find('-')]
        if target_contest != 'all' and contest != target_contest:
            continue

        contest_dir = os.path.join(tasks_dir_path, contest)

        if contest not in files:
            os.mkdir(contest_dir)
            files.append(contest)

        num = short_name[short_name.find('-') + 1:]
        task_dir = os.path.join(contest_dir, num)
        if num not in os.listdir(contest_dir) :
            os.mkdir(task_dir)
        c_file_name = c_file(os.listdir(task_dir))
        if not(c_file_name):
            c_file_name = problem["name"].replace("/", "_") + extension
            open(os.path.join(task_dir, c_file_name), 'w').close()
            with open(os.path.join(task_dir, 'generator.py'), 'a') as generator:
                if os.stat(os.path.join(task_dir, 'generator.py')).st_size < 10:
                    generator.write(generator_text)

            if 'tests' not in os.listdir(task_dir) :
                os.mkdir(task_dir + '/tests')
        if sync_statements or sync_samples:
            task_html = session.get(problem['href'])

            if sync_statements:
                if 'statement.txt' not in os.listdir(task_dir):
                    soup = bs(task_html.content, 'html.parser')

                    start_text = f'Problem {short_name}: {problem["name"]}'
                    finish = soup.text.find('Examples')
                    if finish == -1:
                        finish = soup.text.find('\nSubmit a solution\n\n')
                    statement = soup.text[soup.text.find(start_text) + len(start_text) + 1: finish]

                    with open(os.path.join(task_dir, 'statement.txt'), 'w') as statementfile:
                        statementfile.write(statement)

            if sync_samples:
                soup = bs(task_html.content, 'html.parser')

                if 'Input' in soup.text and 'Output' in soup.text:
                    sample_input = soup.text[soup.text.find('Input') + 6: soup.text.find('Output')]
                    sample_output = (
                        soup.text[soup.text.find('Output') + 7: soup.text.find('\nSubmit a solution\n\n')] + '\n')

                    filein_name = os.path.join(task_dir, 'tests', '000.dat')

                    fileout_name = os.path.join(task_dir, 'tests', '000.ans')

                    with open(filein_name, 'w') as filein:
                        filein.write(sample_input)
                    with open(fileout_name, 'w') as fileout:
                        fileout.write(sample_output)
