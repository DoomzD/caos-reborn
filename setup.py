from setuptools import setup

setup(name = 'caos-reborn',
    version = '1.2',
    url = 'https://github.com/DoomzD/caos-reborn',
    author = 'Alex Koryakov & Artem Melnikov',
    author_email = 'avkoryakov@gmail.com',
    description = 'Multifunctional tool for caos course',
    packages = ['caoslib'],
    scripts = ['caos'],
    install_requires = ['clint', 'beautifulsoup4'])
