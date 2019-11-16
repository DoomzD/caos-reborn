from setuptools import setup

setup(name = 'caos-reborn',
    version = '1.0',
    url = 'https://github.com/DoomzD/caos-reborn',
    author = 'Alex Koryakov',
    author_email = 'avkoryakov@gmail.com',
    description = 'Multifunctional tool for caos course',
    keywords = 'caos',
    packages = 'caoslib',
    scripts = ['caos'],
    install_requires = ['clint', 'beautifulsoup4'])
