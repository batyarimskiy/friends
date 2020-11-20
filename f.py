import os, sys
import vk_api
import requests
import time

from termcolor import colored

banner = colored("""
  █████▒██▀███   ██▓▓█████  ███▄    █ ▓█████▄   ██████
▓██   ▒▓██ ▒ ██▒▓██▒▓█   ▀  ██ ▀█   █ ▒██▀ ██▌▒██    ▒
▒████ ░▓██ ░▄█ ▒▒██▒▒███   ▓██  ▀█ ██▒░██   █▌░ ▓██▄
░▓█▒  ░▒██▀▀█▄  ░██░▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌  ▒   ██▒
░▒█░   ░██▓ ▒██▒░██░░▒████▒▒██░   ▓██░░▒████▓ ▒██████▒▒
 ▒ ░   ░ ▒▓ ░▒▓░░▓  ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░
 ░       ░▒ ░ ▒░ ▒ ░ ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒ ░ ░▒  ░ ░
 ░ ░     ░░   ░  ▒ ░   ░      ░   ░ ░  ░ ░  ░ ░  ░  ░
          ░      ░     ░  ░         ░    ░          ░
                                ░
""", "red")
menu = """
[1] VK
[2] Instagram
[3] TikTok

[4] Разработчик
[5] Выход
"""
with open("ids.txt") as f:
    user_ids = f.read().splitlines()
    print(user_ids)

def add_friends(user_ids):
    token = input('Ваш токен: ')
    session = vk_api.VkApi(token=token)
    vk = session.get_api()
    
    for user_id in user_ids:
        vk.friends.add(
            user_id=user_id
        )
        
        time.sleep(40)

def insta():
    print("""Еще не готово, воркаю

Нажмите Enter для выхода в меню...""")
    input()
    main()

def tiktok():
    print("""Еще не готово, воркаю

Нажмите Enter для выхода в меню...""")
    input()
    main()

def devoloper():
    print("""Разработчик: @batyarimskiy (TG)

Нажмите Enter для выхода в меню...""")
    input()
    main()

def exit():
    os.system('clear')
    print('''
Жду тебя снова!

''')
    sys.exit()

def main():
    os.system('clear')
    print(banner)
    print(menu)
    num_menu = input("/> ")
    if num_menu == "1":
        add_friends(user_ids)
    if num_menu == "2":
        insta()
    if num_menu == "3":
        tiktok()
    if num_menu == "4":
        devoloper()
    if num_menu == '5':
        exit()

main()

