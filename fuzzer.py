from colours import *
from argparse import ArgumentParser
from requests import get
from os import getcwd

accepted = [200, 301]

parser = ArgumentParser(description='A Basic Fuzzer')
parser.add_argument('-u', '--url', type=str, help='The URL')
parser.add_argument('-w', '--wordlist', type=str, help='The wordlist to use for fuzzing')
parser.add_argument('--hide', action='store_true')
args = parser.parse_args()

url = args.url
wordlist = getcwd() + '\\' + args.wordlist
hide = args.hide

with open(wordlist) as f:
    print('-' * 70)
    print(f'| Wordlist: {wordlist}'.ljust(69, ' ') + '|')
    print(f'| URL: {url}'.ljust(69, ' ') + '|')
    print('-' * 70)

    for x in f.read().split('\n'):
        print(f'Testing: {green}{x}{reset}', end='')
        req = get(f'{url}/{x}')
        
        if req.status_code in accepted:
            print(f'\t\t{red}Found!{reset}')
        elif hide:
            print('\r', end='')
        else:
            print()
