import requests
from bs4 import BeautifulSoup

# Get Website Linking and its Content
r = requests.get("https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c = r.content

# Parse and extract the parts of interest
soup = BeautifulSoup(c, "html.parser")


