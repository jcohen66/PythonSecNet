import os

if not os.path.exists('data'):
    try:
        os.makedirs('data')
        print('[+] Directory created')
    except OSError as error:
        print(error)
