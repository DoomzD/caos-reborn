from utils.constants import LINKS_PATH, SUMMARY

from clint.textui import puts, colored
import json


def validate_session(session):
    links = {}
    with open(LINKS_PATH, 'r') as linksfile:
        links = json.load(linksfile)

    result = session.get(links[SUMMARY])
    if 'Invalid session' in result.text:
        puts(colored.red("Your session is outdated. Run './caos init-session'."))
