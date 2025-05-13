import requests
from bs4 import BeautifulSoup

url = 'https://www.instagram.com/anthony.carv/followers/'
response = requests.get(url)
site = BeautifulSoup(response.content,"html.parser")
site.find_all("span", class_="_ap3a _aaco _aacw _aacx _aad7 _aade")
print(site.find_all("span"))