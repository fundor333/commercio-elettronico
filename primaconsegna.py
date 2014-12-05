__author__ = 'Matteo Scarpa 845087'

import re
import codecs
import urllib
import time

import requests
import lxml.html as html
import BeautifulSoup


SESSION = requests.Session()
GOOGLEURL = "https://www.google.it/search?q=site:www.repubblica.it+%2B+politica+OR+crisi+OR+calcio+OR+articolo+OR+articoli&tbm=nws&num=100&start="
OUTPITFILENAME = "out"
NUMERORISULTATI = 100
WAITINGTIME = 3  # in secondi
QUERYGOOGLE = '//h3[@class="r"]/a/@href'
QUERYSITO = '//*[@itemprop="articleBody"]/text()'


class AppURLopener(urllib.FancyURLopener):
    version = "App/1.7"


# ####################################################
def decode_html(nome):
    html_string = file(str(nome) + '.html').read()
    converted = BeautifulSoup.UnicodeDammit(html_string, isHTML=True)
    if not converted.unicode:
        print("Errore conversione unicode")
        return ''
    return converted.unicode


def linkgetter(urlpage, waiting):
    urldictionary = []
    serverresponce = SESSION.get(urlpage)
    time.sleep(waiting)
    queryresult = html.fromstring(serverresponce.text).xpath(QUERYGOOGLE)
    for url in queryresult:
        if url.split("/search?q=")[0] != "":
            url = url.split("/url?q=")[1]
            url = url.split('&sa=')[0]
            urldictionary.append(url)
    return urldictionary


def getarticle(url, number):
    if url == "":
        return number
    else:
        urllib.urlretrieve(url, "./html/" + str(number) + '.html')
        urlhtml = html.fromstring(decode_html("./html/" + str(number)))
        articlebody = urlhtml.xpath(QUERYSITO)
        if articlebody == []:
            return number
        else:
            fileout = codecs.open('./out/' + str(number) + '.txt', 'w', 'utf-8')
            reference = ""
            stopword = open("spamword.teo")
            stoplist = None
            for line in stopword:
                stoplist = set(line.split())
            for parolanonelaborata in str(articlebody).split():
                for singolaparola in re.split("[^a-zA-Z]", parolanonelaborata):
                    if singolaparola != '' or singolaparola not in stoplist:
                        reference = reference + " " + singolaparola.lower()

            print >> fileout, reference
            fileout.close()
            return number + 1


def getfromgoogle(numberpages):
    urddictionary = {}

    for i in range(0, numberpages):
        print("From Google n " + str(i) + " out of " + str(NUMERORISULTATI))
        for element in linkgetter(GOOGLEURL + str(i * 10), WAITINGTIME):
            urddictionary[element] = i
    outdictionary = {}
    num = 0

    for url in urddictionary.keys():
        print("From Url n " + str(num))
        num = getarticle(url, num)
    maindict = {}

    for i in range(0, num - 1):
        filein = open("./out/" + str(i) + '.txt')
        refline = ""
        for line in filein:
            refline += line
        outdictionary[i] = refline
    numberfile = i

    for text in outdictionary.items():
        maindict = adddictionary(maindict, getsingledict(text[1]))
    printdict(maindict, OUTPITFILENAME, numberfile)
    return numberfile


def adddictionary(maindict, secondarydictionary):
    for element in secondarydictionary:
        if element in maindict.keys():
            maindict[element] = (
                maindict[element][0] + 1, maindict[element][1] + secondarydictionary[element])
        else:
            maindict[element] = (1, secondarydictionary[element])
    return maindict


def getsingledict(imputtext):
    dictionary = {}
    for word in imputtext.split():
        if word in dictionary.keys():
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary


def printdict(dictionary, filename, number):
    fileout = codecs.open('./out/' + filename + '.txt', 'w', 'utf-8')
    fileout.write(str(number) + '\n')
    for key in dictionary:
        fileout.write(key + " " + str(dictionary[key][0]) + " " + str(dictionary[key][1]) + '\n')
    fileout.close()


# Esecutore intero progetto
if __name__ == "__main__":
    urllib._urlopener = AppURLopener()
    getfromgoogle(NUMERORISULTATI)