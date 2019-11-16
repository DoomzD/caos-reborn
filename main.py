import requests
from src.caos import caos


if __name__ == "__main__":
    session = requests.session()
    caos(session)