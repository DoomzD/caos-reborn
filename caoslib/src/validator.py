from defined.post_init import COOKIES_PATH
from defined.constants import SUMMARY
from utils import read_links

from clint.textui import puts, colored
import json
import os

def validate_cookies():
    #just checking if not empty
    if os.stat(COOKIES_PATH).st_size < 20:
        return 0
    return 1

def validate_session(session):
    links = read_links()

    result = session.get(links[SUMMARY])
    if 'Invalid session' in result.text:
        return 0
    return 1
