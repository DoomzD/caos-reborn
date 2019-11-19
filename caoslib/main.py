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

    flags = args.flags
    if 'status' in args:
        summary(session, '--solved' in flags or '-s' in flags)
    elif 'sync' in args:
        sync_samples = '--sync-samples' in flags or '-ssa' in flags or '--sync-all' in flags or '-sa' in flags
        sync_statements = '--sync-statements' in flags or '-sst' in flags or '--sync-all' in flags or '-sa' in flags
        sync(session, sync_samples, sync_statements)
    elif 'standings' in args:
        standings(session)
    elif 'test' in args:
        test(args)

    # menu = login(session)
    # print(menu)
