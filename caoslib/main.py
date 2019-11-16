from src.initialization import init, init_session
from src.validator import validate_session
from utils.constants import COOKIES_PATH, LINKS_PATH, SUMMARY

from bs4 import BeautifulSoup as bs
from clint import arguments
from clint.textui import puts, colored
import pickle, json
import requests


if __name__ == '__main__':
    args = arguments.Args()

    print(args)
    if 'init' in args:
        init()
        puts(colored.green("Successfully logged in"))
        exit(0)

    if 'init-session' in args:
        init_session()
        puts(colored.green("Successfully logged in"))
        exit(0)

    session = requests.session()
    with open(COOKIES_PATH, 'rb') as  cookiesfile:
        session.cookies.update(pickle.load(cookiesfile))

    validate_session(session)

    # menu = login(session)
    # print(menu)
    