from defined.constants import STANDINGS
from utils import read_links

from bs4 import BeautifulSoup as bs
from clint.textui import puts, colored


def standings(session):
    links = read_links()
    standings_html = session.get(links[STANDINGS])

    soup = bs(standings_html.content, 'html.parser')

    name = soup.title.text[:soup.title.text.find('[') - 1]

    users = soup.find_all('td', {'class': 'st_team'})
    totals = soup.find_all('td', {'class': 'st_total'})
    scores = soup.find_all('td', {'class': 'st_score'})

    for place, (user, total, score) in enumerate(zip(users, totals, scores)):
        row = "{: >5}.{: >25}: {}({})".format(place + 1, user.text, total.text, score.text)
        if user.text != name:
            puts(colored.blue(row))
        else:
            puts(colored.red(row))
