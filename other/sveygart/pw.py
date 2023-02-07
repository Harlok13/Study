# pw.py - программа для незащищенного хранения паролей

import sys
import pyperclip

PASSWORDS = {}

if len(sys.argv) < 2:
    print('Использование: python pw.py [имя учетной записи] - копирование пароля учетной записи')
    sys.exit()

account = sys.argv[1]
