from setuptools import setup, find_packages

setup(name = 'caos-reborn',
    version = '1.9.1',
    url = 'https://github.com/DoomzD/caos-reborn',
    author = 'Artem Melnikov & Alex Koryakov',
    author_email = 'melnikovam10@gmail.com',
    description = 'Multifunctional tool for caos course',
    package_data={'': ['clang-format']},
    packages = find_packages(),
    scripts = ['caos'],
    install_requires = ['clint', 'beautifulsoup4'])
