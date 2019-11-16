from utils.constants import SUMMARY, OK, REVIEW, NOT_SUBMITTED
from utils.utils import read_links

from bs4 import BeautifulSoup as bs
from clint.textui import puts, colored, indent

def summary(session, show_solved):
    links = read_links()
    summary_page = session.get(links[SUMMARY])

    soup = bs(summary_page.content, 'html.parser')
    problem_containers = soup.find_all('td', {'class': 'b1'})

    problem = 0
    problems = []
    while problem < len(problem_containers):
        problem_name = problem_containers[problem + 1].text
        problem_status = NOT_SUBMITTED if problem_containers[problem + 2].text == '\xa0' else problem_containers[problem + 2].text
        problems.append((problem_name, problem_status))
        problem += 6

    problem_template = "{: <32}{}"
    for problem in problems:
        formatted_problem = problem_template.format(problem[0] + ":", problem[1])
        
        if problem[1] == OK and show_solved:
            with indent(4, quote='✔'):
                puts(colored.green(formatted_problem))
        elif problem[1] == REVIEW and show_solved:
            with indent(4, quote='?'):
                puts(colored.yellow(formatted_problem))
        elif problem[1] not in [OK, REVIEW]:
            with indent(4, quote='✖'):
                puts(colored.red(formatted_problem))
