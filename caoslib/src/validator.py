from utils.constants import COOKIES_PATH, SUMMARY
from utils.utils import read_links

from clint.textui import puts, colored
import json


def validate_cookies():
    try:
        open(COOKIES_PATH, 'r').close()
    except:
        puts(colored.red("No cookies found. Run './caos init-session'."))
        exit(1)


def validate_session(session):
    links = read_links()

    result = session.get(links[SUMMARY])
    if 'Invalid session' in result.text:
        return 0
    return 1
