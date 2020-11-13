from defined.constants import SUMMARY, OK, REVIEW, NOT_SUBMITTED
from utils import get_problems

from bs4 import BeautifulSoup as bs
from clint.textui import puts, colored, indent

def summary(session, show_solved):
    problems = get_problems(session)

    problem_template = "{: <32}{}({})"
    problems_solved = 0
    total_score = 0
    for problem in problems:
        formatted_problem = problem_template.format(
            problem['name'] + ":",
            problem['status'],
            problem['score']
        )

        total_score += int(problem['score'])
        problems_solved += problem['status'] in [OK, REVIEW]

        if problem['status'] == OK and show_solved:
            with indent(4, quote='✔'):
                puts(colored.green(formatted_problem))
        elif problem['status'] == REVIEW and show_solved:
            with indent(4, quote='?'):
                puts(colored.yellow(formatted_problem))
        elif problem['status'] not in [OK, REVIEW]:
            with indent(4, quote='✖'):
                puts(colored.red(formatted_problem))

    puts('{:_>50}'.format(''))
    puts(colored.green(
        f'Total tasks: {len(problems)}, Solved tasks: {problems_solved}, Total score: {total_score}'
    ))
