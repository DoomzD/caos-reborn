from src.initialization import init, init_session
from src.validator import validate_cookies, validate_session
from src.summary import summary
from src.sync import sync
from src.standings import standings
from src.test import test
from utils.constants import COOKIES_PATH

from bs4 import BeautifulSoup as bs

from clint import arguments
from clint.textui import puts, colored

import logging
import pickle, json
import requests


if __name__ == '__main__':
    args = arguments.Args()
    if 'init' in args:
        init()
        puts(colored.green("Successfully logged in"))
    elif 'init-session' in args:
        init_session()
        puts(colored.green("Successfully logged in"))

    validate_cookies()

    # recover previous session
    session = requests.session()
    with open(COOKIES_PATH, 'rb') as  cookiesfile:
        session.cookies.update(pickle.load(cookiesfile))

    validate_session(session)

    if 'status' in args:
        summary(session, '--solved' in args)
    elif 'sync' in args:
        sync(session, '--sync-samples' in args, '--sync-statements' in args)
    elif 'standings' in args:
        standings(session)
    elif 'test' in args:
        test(args)

    # menu = login(session)
    # print(menu)
