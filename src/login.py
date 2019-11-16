import configparser
from bs4 import BeautifulSoup as bs

from src.utils.constants import CONFIG_FILE


def login(session):
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    credentials = {
        'login': config['Credentials']['login'],
        'password': config['Credentials']['password']
    }

    url = 'https://caos.ejudge.ru/ej/client?contest_id=1{:02d}'.format(int(config['Group']['group_number']))
    start_page = session.post(
        url,
        data=credentials,
        headers=dict(referer=url),
    )

    soup = bs(start_page.content, 'html.parser')

    links = soup.find_all('a', {'class': 'menu'})[:-1]
    return dict(map(lambda x: (x.text, x['href']), links))
