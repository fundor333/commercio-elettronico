#!/usr/bin/python
import codecs
import string
import urllib
import lxml.html as H
# import lxml.etree as ET
import BeautifulSoup
# import codecs

GOOGLEURL = "https://www.google.it/search?q=site:www.ansa.it+mafia&sa=G&gbv=2&sei=Z4k3VKCtDc20aYaPgKgL"
FILEURL = "url.txt"
NUMERORISULTATI = 100


class WebPage:
    filen = ""

    def __init__(self, url, name):
        self.filen = name
        urllib.urlretrieve(url, name + '.html')
        elaborato = self.decode_html(name + '.html')
        outputfile = codecs.open(name + ".txt", 'w', 'utf-8')
        outputfile.write(elaborato)
        outputfile.close()

    def decode_html(self, filename):
        html_string = file(filename).read()
        converted = BeautifulSoup.UnicodeDammit(html_string, isHTML=True)
        if not converted.unicode:
            print("Errore")
            return ''
        print converted.originalEncoding
        return converted.unicode


class ElaboratoreFile:
    filename = ""

    def __init__(self,name):
        self.filename = name

    def googleextractor(self):
        return self

    def elaboratore(self,file,stringacercata):
        root = H.fromstring
        res = root.xpath(stringacercata)
        if res:
            for fr in res:
                fieldRank = int(fr.xpath('td[1]//div[@class="left"]')[0].text)
                name = string.join(fr.xpath('td[2]')[0].itertext()).strip()



class AppURLopener(urllib.FancyURLopener):
    version = "App/1.7"


def main():
    urllib._urlopener = AppURLopener()
    nomefile = "risultati"
    google = WebPage(GOOGLEURL, nomefile)
    ElaboratoreFile(nomefile).googleextractor()

# Esecutore intero progetto
if __name__ == "__main__":
    main()