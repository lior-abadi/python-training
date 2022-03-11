import requests
from bs4 import BeautifulSoup

r = requests.get("https://pythonizing.github.io/data/example.html")
c = r.content

soup = BeautifulSoup(c, "html.parser")
soup.find_all("div") 

