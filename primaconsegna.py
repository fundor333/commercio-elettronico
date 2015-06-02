from google import search
import requests
import lxml.html

SESSION = requests.Session()
GOOGLE_SEARCH_STRING = "site:www.repubblica.it + politica OR crisi OR calcio OR articolo OR article"
NUMERORISULTATI = 120
WAITINGTIME = 2  # in secondi
QUERYSITO = '//*[@itemprop="articleBody"]/text()'


# ####################################################

article_url=search(GOOGLE_SEARCH_STRING, stop=NUMERORISULTATI, pause=WAITINGTIME)
text=[]
for url in article_url:
    html = lxml.html.parse(url)
    packages = html.xpath(QUERYSITO)
    if packages:
        text.append(packages)
