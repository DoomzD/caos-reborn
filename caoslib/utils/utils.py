from utils.constants import LINKS_PATH

import json


def read_links():
    links = {}
    with open(LINKS_PATH, 'r') as linksfile:
        links = json.load(linksfile)
    return links
