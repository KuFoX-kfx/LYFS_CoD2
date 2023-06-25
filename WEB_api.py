import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import os

class WEB_api:
    def __init__(self):
        ua = UserAgent()
        global headers
        headers = {'User-Agent':str(ua.random)}
        
    def GetName(self, URL):
        self.response = requests.get(URL, headers=headers)
        self.soup = BeautifulSoup(self.response.text, 'lxml')
        return self.soup.find('td', id="hostname").text
    
    def GetPlayers(self, URL):
        self.response = requests.get(URL, headers=headers)
        self.soup = BeautifulSoup(self.response.text, 'lxml')
        return self.soup.find('td', id="players").text
    
    def GetGM(self, URL):
        self.response = requests.get(URL, headers=headers)
        self.soup = BeautifulSoup(self.response.text, 'lxml')
        return self.soup.find('td', id="gamemode").text
    
    def GetMap(self, URL):
        self.response = requests.get(URL, headers=headers)
        self.soup = BeautifulSoup(self.response.text, 'lxml')
        return self.soup.find('td', id="mapname").text
    
    def IntCHK(self, IP):
        return os.system("ping -n 1 " + IP)

        