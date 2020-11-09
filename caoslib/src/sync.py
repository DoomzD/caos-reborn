from defined.constants import CAOS_DIR
from .utils import get_problems

import os
from bs4 import BeautifulSoup as bs


def sync(session, sync_samples, sync_statements, target_contest='all', extension='.c'):
    files = os.listdir(CAOS_DIR)
    problems = get_problems(session)

    for problem in problems:
        short_name = problem['short name']
        contest = short_name[:short_name.find('-')]
        if target_contest != 'all' and contest != target_contest:
            continue

        contest_dir = os.path.join(CAOS_DIR, contest)

        if contest not in files:
            os.mkdir(contest_dir)
            files.append(contest)

        num = short_name[short_name.find('-') + 1:]
        task_dir = os.path.join(contest_dir, num)
        if num not in os.listdir(contest_dir):
            os.mkdir(task_dir)
            open(os.path.join(task_dir, 'main' + extension), 'a').close()
            open(os.path.join(task_dir, 'generator.py'), 'a').close()

            os.mkdir(task_dir + '/tests')

        if sync_statements:
            task_html = session.get(problem['href'])
            soup = bs(task_html.content, 'html.parser')

            start = f'Problem {short_name}: {problem["name"]}'
            finish = '\nSubmit a solution\n\n'
            statement = soup.text[soup.text.find(start) + len(start) + 1: soup.text.find(finish)]

            with open(os.path.join(task_dir, 'statement.txt'), 'w') as statementfile:
                statementfile.write(statement)

        if sync_samples:
            task_html = session.get(problem['href'])
            soup = bs(task_html.content, 'html.parser')

            if 'Input' in soup.text and 'Output' in soup.text:
                sample_input = soup.text[soup.text.find('Input') + 6: soup.text.find('Output')]
                sample_output = (
                    soup.text[soup.text.find('Output') + 7: soup.text.find('\nSubmit a solution\n\n')] + '\n')

                filein_name = os.path.join(task_dir, 'tests', '000.dat')
                open(filein_name, 'a').close()

                fileout_name = os.path.join(task_dir, 'tests', '000.ans')
                open(fileout_name, 'a').close()

                with open(filein_name, 'w') as filein:
                    filein.write(sample_input)
                with open(fileout_name, 'w') as fileout:
                    fileout.write(sample_output)
