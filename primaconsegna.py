import re

import requests


__author__ = 'Matteo Scarpa 845087'

import codecs
import time
import lxml.html as html

SESSION = requests.Session()
GOOGLEURL = "https://www.google.it/search?q=site:www.repubblica.it+crisi&num=100&start="
OUTPITFILENAME = "out"
NUMERORISULTATI = 100
WAITINGTIME = 3  # in secondi
QUERYGOOGLE = '//h3[@class="r"]/a/@href'
QUERYSITO = '//*[@itemprop="articleBody"]/text()'

# ####################################################


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
        serverresponce = SESSION.get(url)
        urlhtml = html.fromstring(serverresponce.text)
        if not urlhtml.xpath(QUERYSITO):
            return number
        else:
            articlebody = urlhtml.xpath(QUERYSITO)
            fileout = codecs.open('./out/' + str(number) + '.txt', 'w', 'utf-8')
            reference = ""
            for parolanonelaborata in str(articlebody).split():
                for singolaparola in re.split("[^a-zA-Z]", parolanonelaborata):
                    if singolaparola != '':
                        reference = reference + " " + singolaparola.lower()

            print >> fileout, reference
            fileout.close()
            return number + 1


def getfromgoogle(numberpages):
    urddictionary = {}

    for i in [0, numberpages]:
        for element in linkgetter(GOOGLEURL + str(i * 10), WAITINGTIME):
            urddictionary[element] = i
    outdictionary = {}
    num = 0

    for url in urddictionary.keys():
        num = getarticle(url, num)
    maindict = {}

    for i in [0, num-1]:
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


def printdict(dictionary, filename, number):
    fileout = codecs.open('./out/' + filename + '.txt', 'w', 'utf-8')
    fileout.write(number)
    for key in dictionary:
        fileout.write(key + " "+ str(dictionary[key][0])+ " "+ str(dictionary[key][1]) + '\n')
    fileout.close()


# Esecutore intero progetto
if __name__ == "__main__":
    getfromgoogle(NUMERORISULTATI)