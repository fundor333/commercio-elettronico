#!/usr/bin/python
import codecs
import urllib
import lxml.html as html
import BeautifulSoup
import time

GOOGLEURL = "https://www.google.it/search?q=site:www.ansa.it+crisi&sasite:www.ansa.it+mafia&gbv=&start="
TAGCLASS = "articleBody"
FILEURL = "url"
NUMERORISULTATI = 100  # il valore indicato va moltiplicato per 10
WAITINGTIME = 2  # in secondi
QUERYGOOGLE = '//h3[@class="r"]/a/@href'
QUERYSITO = '//div[@itemprop="articleBody"]/text()'
CERCAINGOOGLE = 1  # Mettere a 0 per poter scaricare risultati aggiornati
CERCAINRESULT = 0  # Mettere a 0 per poter scaricare i file aggiornati


class AppURLopener(urllib.FancyURLopener):
    version = "App/1.7"


class Contaparole:
    listanome = ""
    fileinput = None
    main_dict = None

    def __init__(self, listnomi, dizionario):
        self.listanome = listnomi
        self.main_dict = dizionario
        for nome in listnomi:
            self.fileinput = open(nome + ".txt", 'r')
            dictionary = {}
            for line in self.fileinput:

                for singolaparola in line.split():
                    if singolaparola in dictionary.keys():
                        dictionary[singolaparola] += 1
                    else:
                        dictionary[singolaparola] = 1

            self.adddizionario(dictionary)

    def appoggiodict(self, line, dictionary):
        for singolaparola in line.split():
            if singolaparola in dictionary.keys():
                dictionary[singolaparola] += 1
            else:
                dictionary[singolaparola] = 1

    def adddizionario(self, dizzio):
        for campo in dizzio:
            if campo in self.main_dict.keys():
                self.main_dict[campo] = (
                    self.main_dict[campo][0] + 1, self.main_dict[campo][1] + dizzio[campo])
            else:
                self.main_dict[campo] = (1, dizzio[campo])

    def printer(self, filename):
        nome = open(filename, "w")
        for riga in self.main_dict:
            nome.writelines(riga + str(self.main_dict[riga]) + "\n")
        nome.close()


class ElaboratoreRicerca:
    listafilename = None
    url = None

    def __init__(self, url, listanemaname):
        self.listafilename = listanemaname
        self.url = url
        urllib._urlopener = AppURLopener()

    def googleesecutore(self):
        if CERCAINGOOGLE == 0:
            print("Start downloading from Google")
            for i in range(NUMERORISULTATI):
                print("Waiting number " + str(i + 1) + " of " + str(NUMERORISULTATI))
                time.sleep(WAITINGTIME)
                urllib.urlretrieve(self.url[i], self.listafilename[i] + '.html')
                self.printer(self.listafilename[i])
            self.estrattore()
        for i in range(NUMERORISULTATI):
            self.printer(self.listafilename[i])

    def estrattore(self):
        output = open(FILEURL + ".txt", 'w')
        for i in range(1, NUMERORISULTATI):
            self.elaboratorequery(decode_html(self.listafilename[i]), QUERYGOOGLE, output)
        output.close()

    def elaboratorequery(self, inputfile, query, output):
        files = html.fromstring(inputfile)
        for url in files.xpath(query):
            output.write(url + "\n")

    def printer(self, nome):
        outputfile = codecs.open(nome + ".txt", 'w', 'utf-8')
        outputfile.write(decode_html(nome))
        outputfile.close()

    def risultatiesecutore(self):
        if CERCAINRESULT == 0:
            print("Start downloading from result")
            appoggio = open(FILEURL + ".txt", 'r')
            listaurl = range(len(appoggio.readlines()))
            for i in range(len(appoggio.readlines())):
                print("Waiting number " + str(i + 1) + " of " + str(NUMERORISULTATI))
                time.sleep(WAITINGTIME)
                urllib.urlretrieve(self.url[i], self.listafilename[i] + '.html')
                self.printer(self.listafilename[i])
            self.estrattore()
        for i in range(len(appoggio.readlines())):
            self.printer(self.listafilename[i])


def decode_html(nome):
    html_string = file(nome + '.html').read()
    converted = BeautifulSoup.UnicodeDammit(html_string, isHTML=True)
    if not converted.unicode:
        print("Errore conversione unicode")
        return ''
    return converted.unicode


def main():
    listaurl = range(NUMERORISULTATI * 10)
    listanomi = range(NUMERORISULTATI * 10)

    for i in range(NUMERORISULTATI):
        listaurl[i] = GOOGLEURL + str(i * 10)
        listanomi[i] = "risultati" + str(i)
    appoggio = ElaboratoreRicerca(listaurl, listanomi)
    appoggio.googleesecutore()

    appoggio = open(FILEURL + ".txt", 'r')

    listaurl = range(len(appoggio.readlines()))
    listanomi = range(len(appoggio.readlines()))

    for i in range(len(appoggio.readlines())):
        listaurl[i] = appoggio.readlines()[i]
        listanomi[i] = "risultatielaborati" + str(i)

    appoggio = ElaboratoreRicerca(listaurl, listanomi)
    appoggio.risultatiesecutore()

    diz = {}
    Contaparole(listanomi, diz).printer("output.txt")

# Esecutore intero progetto
if __name__ == "__main__":
    main()