from setuptools import setup, find_packages

setup(name = 'caos-reborn',
    version = '1.5.3',
    url = 'https://github.com/DoomzD/caos-reborn',
    author = 'Alex Koryakov & Artem Melnikov',
    author_email = 'avkoryakov@gmail.com & melnikovam10@gmail.com',
    description = 'Multifunctional tool for caos course',
    packages = find_packages(),
    scripts = ['caos'],
    install_requires = ['clint', 'beautifulsoup4'])
