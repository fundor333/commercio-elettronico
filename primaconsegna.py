import urllib
from urllib.request import FancyURLopener
from bs4 import BeautifulSoup
from google import search
import requests

SESSION = requests.Session()
GOOGLE_SEARCH_STRING = "site:www.repubblica.it + politica OR crisi OR calcio OR articolo OR article"
NUMERORISULTATI = 1
WAITINGTIME = 2  # in secondi
QUERYGOOGLE = '//h3[@class="r"]/a/@href'
QUERYSITO = '//*[@itemprop="articleBody"]/text()'


# ####################################################

article_url=search(GOOGLE_SEARCH_STRING, stop=NUMERORISULTATI, pause=WAITINGTIME)
print(article_url)
for url in article_url:
    html_page = urllib.request.urlopen(url)
    html_string = html_page.read()
    converted = BeautifulSoup.UnicodeDammit(html_string, isHTML=True)
    if not converted.str:
        print("")
    print(converted.str)