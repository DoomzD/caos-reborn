from utils.constants import SUMMARY, OK, REVIEW, NOT_SUBMITTED
from utils.utils import get_problems

from bs4 import BeautifulSoup as bs
from clint.textui import puts, colored, indent

def summary(session, show_solved):
    problems = get_problems(session)

    problem_template = "{: <32}{}({})"
    for problem in problems:
        formatted_problem = problem_template.format(
            problem['name'] + ":", 
            problem['status'], 
            problem['score']
        )

        if problem['status'] == OK and show_solved:
            with indent(4, quote='✔'):
                puts(colored.green(formatted_problem))
        elif problem['status'] == REVIEW and show_solved:
            with indent(4, quote='?'):
                puts(colored.yellow(formatted_problem))
        elif problem['status'] not in [OK, REVIEW]:
            with indent(4, quote='✖'):
                puts(colored.red(formatted_problem))
