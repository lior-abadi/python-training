import requests
from bs4 import BeautifulSoup

# Get Website Linking and its Content
r = requests.get("https://pythonizing.github.io/data/example.html")
c = r.content

# Parse and extract the parts of interest
soup = BeautifulSoup(c, "html.parser")
all = soup.find_all("div", {"class": "cities"}) 

for item in all:
    print(item.find_all("h2")[0].text)
