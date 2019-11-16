from utils.constants import SUMMARY
from utils.utils import read_links

from clint.textui import puts, colored
import json


def validate_session(session):
    links = read_links()

    result = session.get(links[SUMMARY])
    if 'Invalid session' in result.text:
        puts(colored.red("Your session is outdated. Run './caos init-session'."))
