#!/usr/bin/python
import codecs
import urllib
# import lxml.html as h
# import lxml.etree as ET
import BeautifulSoup
# import codecs

from calcolatore import Contaparole

GOOGLEURL = "https://www.google.it/search?q=site:www.ansa.it+mafia&sa=G&gbv=2&sei=Z4k3VKCtDc20aYaPgKgL"
TAGCLASS = "articleBody"
FILEURL = "url.txt"
NUMERORISULTATI = 100


class WebPage:
    filen = ""

    def __init__(self, url, name):
        self.filen = name
        urllib.urlretrieve(url, name + '.html')
        elaborato = decode_html(name + '.html')
        outputfile = codecs.open(name + ".txt", 'w', 'utf-8')
        outputfile.write(elaborato)
        outputfile.close()


class ElaboratoreFile:
    filename = ""

    def __init__(self, name):
        self.filename = name

    def googleextractor(self):
        return self


class AppURLopener(urllib.FancyURLopener):
    version = "App/1.7"


def decode_html(filename):
    html_string = file(filename).read()
    converted = BeautifulSoup.UnicodeDammit(html_string, isHTML=True)
    if not converted.unicode:
        print("Errore conversione unicode")
        return ''
    return converted.unicode


def main():
    lista = ""  # TODO elenco dei URL dei file che ho trovato con google
    nomefile = "risultati"

    urllib._urlopener = AppURLopener()
    google = WebPage(GOOGLEURL, nomefile)

    ElaboratoreFile(nomefile).googleextractor()

    diz = {}
    for i in lista:
        dizzio = Contaparole(i + ".txt", diz)
        dizzio.printer("output.txt")

# Esecutore intero progetto
if __name__ == "__main__":
    main()