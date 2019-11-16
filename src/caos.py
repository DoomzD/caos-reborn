from src.login import login


def caos(session):
    menu = login(session)
    print(menu)