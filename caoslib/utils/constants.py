import os

# important paths
CONFIG_PATH = os.getcwd() + '/caoslib/files/config.ini'
COOKIES_PATH = os.getcwd() + '/caoslib/files/cookies.owo'
LINKS_PATH = os.getcwd() + '/caoslib/files/links.json'
CAOS_DIR = os.getenv('HOME') + '/programming/hse/caos'

# links
SETTINGS = 'Settings'
SUMMARY = 'Summary'
SUBMISSIONS = 'Submissions'
STANDINGS = 'User standings'
CLAR = 'Submit clar'
CLARS = 'Clars'

# submission status
OK = 'OK'
REVIEW = 'Pending review'
NOT_SUBMITTED = 'Not submitted'

COMPILATION_STRING = "gcc -O2 -Wall -Werror -Wno-unused-result -std=gnu11 -lm {}"