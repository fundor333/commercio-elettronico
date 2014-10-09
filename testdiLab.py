#!/usr/bin/python
import urllib
# import lxml.html as H
# import lxml.etree as ET
import BeautifulSoup
# import codecs

class WebPage:
    filen = ""

    def __init__(self, url, name):
        urllib.urlretrieve(url, name)
        self.filen = name

    def decode_html(filename):
        html_string = file(filename).read()
        converted = BeautifulSoup.UnicodeDammit(html_string, isHTML=True)
        if not converted.unicode:
            return ''
        # print converted.originalEncoding
        return converted.unicode


class AppURLopener(urllib.FancyURLopener):
    version = "App/1.7"


def main():
    urllib._urlopener = AppURLopener()
    web = WebPage(
        "https://www.google.it/search?q=site%3Awww.ansa.it+mafia&btnG=Cerca&gbv=1",
        "risultati.html")

# Esecutore intero progetto
if __name__ == "__main__":
    main()