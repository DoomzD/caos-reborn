from clint.textui import puts, colored
import logging
import pickle, json
import requests
from bs4 import BeautifulSoup as bs

options = ['login', 'status', 'sync', 'standings']

#need edjude for extra data
def handler(mode, flags):
    from defined.paths import COOKIES_PATH
    from .auth import init_session, login
    from .validator import validate_cookies, validate_session
    from .summary import summary
    from .sync import sync
    from .standings import standings
    from .style import style
    from .test import test

    if mode == 'login':
        login()
        puts(colored.green("Successfully saved password and logged in"))
        init_session()

    if not validate_cookies():
        init_session()

    # recover previous session
    session = requests.session()
    with open(COOKIES_PATH, 'rb') as cookiesfile:
        session.cookies.update(pickle.load(cookiesfile))

    if not validate_session(session):
        init_session()

    if mode == 'status':
        summary(session, '--solved' in flags or '-s' in flags)
    elif mode == 'sync':
        sync_samples = '--sync-samples' in flags or '-ssa' in flags or '--sync-all' in flags or '-sa' in flags
        sync_statements = '--sync-statements' in flags or '-sst' in flags or '--sync-all' in flags or '-sa' in flags
        sync(session, sync_samples, sync_statements)
    elif mode == 'standings':
        standings(session)

    exit(0)
