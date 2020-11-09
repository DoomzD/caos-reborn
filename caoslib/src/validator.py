from defined.paths import COOKIES_PATH
from defined.constants import SUMMARY
from .utils import read_links

from clint.textui import puts, colored
import json


def validate_cookies():
    with open(COOKIES_PATH, 'r') as cookies:
        if cookies == "":
            return 0
    return 1

def validate_session(session):
    links = read_links()

    result = session.get(links[SUMMARY])
    if 'Invalid session' in result.text:
        return 0
    return 1
