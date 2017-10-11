import requests
from bs4 import BeautifulSoup
import re

resp = urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")
soup=BeautifulSoup(resp,"html_parser")
