from defined.constants import SUMMARY, NOT_SUBMITTED
from defined.post_init import LINKS_PATH

from bs4 import BeautifulSoup as bs
import json


def read_links():
    links = {}
    with open(LINKS_PATH, 'r') as linksfile:
        links = json.load(linksfile)
    return links


def get_problem_containers(session):
    links = read_links()
    summary_page = session.get(links[SUMMARY])

    soup = bs(summary_page.content, 'html.parser')
    problem_containers = soup.find_all('td', {'class': 'b1'})

    return problem_containers


def get_problems(session):
    problem_containers = get_problem_containers(session)

    problem = 0
    problems = []
    while problem < len(problem_containers):
        short_name = problem_containers[problem].text
        name = problem_containers[problem + 1].text
        href = problem_containers[problem + 1].a['href']
        status = NOT_SUBMITTED if problem_containers[problem + 2].text == '\xa0' else problem_containers[problem + 2].text
        tests_passed = 0 if problem_containers[problem + 3].text == '\xa0' else problem_containers[problem + 3].text
        score = 0 if problem_containers[problem + 4].text == '\xa0' else problem_containers[problem + 4].text

        problems.append({
            'short name': short_name,
            'name': name,
            'href': href,
            'status': status,
            'tests passed': tests_passed,
            'score': score,
        })

        problem += 6

    return problems

def c_file(folder):
    for file_name in folder:
        if file_name[-2:] == ".c":
            return file_name
    return 0
