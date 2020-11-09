from src.initialization import init
from src.standings import standings
from src.style import style
from src.test import test

from bs4 import BeautifulSoup as bs

from clint import arguments
from clint.textui import puts, colored

import logging
import pickle, json
import requests

if __name__ == '__main__':
    args = arguments.Args()
    flags = args.flags
    if 'init' in args:
        init_project()
        puts(colored.green("Init successful"))
    elif 'test' in args:
        test(args)
    elif 'style' in args:
        style(args)
    else:
        from src.web import init_session, login
        from src.validator import validate_cookies, validate_session
        from src.summary import summary
        from utils.constants import COOKIES_PATH
        from src.sync import sync

        if 'login' in args:
            login()
            puts(colored.green("Successfully saved password and logged in"))
            init_session()

        #need edjude for extra data
        validate_cookies()

        # recover previous session
        session = requests.session()
        with open(COOKIES_PATH, 'rb') as cookiesfile:
            session.cookies.update(pickle.load(cookiesfile))

        if not validate_session(session):
            init_session()

        if 'status' in args:
            summary(session, '--solved' in flags or '-s' in flags)
        elif 'sync' in args:
            sync_samples = '--sync-samples' in flags or '-ssa' in flags or '--sync-all' in flags or '-sa' in flags
            sync_statements = '--sync-statements' in flags or '-sst' in flags or '--sync-all' in flags or '-sa' in flags
            sync(session, sync_samples, sync_statements)
        elif 'standings' in args:
            standings(session)

    # menu = login(session)
    # print(menu)
