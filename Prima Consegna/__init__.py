#!/usr/bin/python
import codecs
import string
import urllib
import lxml.html as html
import BeautifulSoup
import time

GOOGLEURL = "https://www.google.it/search?q=site:www.repubblica.it+crisi&sasite:www.ansa.it+mafia&gbv=&start="
TAGCLASS = "articleBody"
FILEURL = "url"
NUMERORISULTATI = 100  # il valore indicato va moltiplicato per 10
WAITINGTIME = 2  # in secondi
QUERYGOOGLE = '//h3[@class="r"]/a/@href'
QUERYSITO = '//*[@itemprop="articleBody"]/text()'
CERCAINGOOGLE = 1  # Mettere a 0 per poter scaricare risultati aggiornati
CERCAINRESULT = 1  # Mettere a 0 per poter scaricare i file aggiornati


class AppURLopener(urllib.FancyURLopener):
    version = "App/1.7"


class Contaparole:
    listanome = ""
    fileinput = None
    main_dict = None

    def __init__(self, listnomi, dizionario):
        self.listanome = listnomi
        self.main_dict = dizionario
        print("Work in progress")
        for nome in listnomi.keys():
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
        nome.writelines("Parola NumeroPagine NumeroRicorrenze\n")
        for riga in self.main_dict:
            nome.writelines(riga + " " + str(self.main_dict[riga][0]) + " " + str(self.main_dict[riga][1]) + "\n")
        nome.close()


class ElaboratoreRicerca:
    listafilename = None
    url = None

    def __init__(self, url, listanemaname):
        self.listafilename = listanemaname
        self.url = url
        urllib._urlopener = AppURLopener()

    def elaboratorequery(self, inputfile, query, output):
        files = html.fromstring(inputfile)
        for risposta in files.xpath(query):
            if risposta[1:7] != "/search":
                output.write(risposta + '\n')

    def printer(self, nome):
        outputfile = codecs.open(nome + ".txt", 'w', 'utf-8')
        outputfile.write(decode_html(nome))
        outputfile.close()


    def googleesecutore(self, flag, numeromassimo, waiting, fileurlout, query):
        if flag == 0:
            print("Start downloading from result")
            for i in range(len(self.url.keys())):
                print("Waiting number " + str(i + 1) + " of " + str(numeromassimo))
                time.sleep(waiting)
                urllib.urlretrieve(self.url.keys()[i], str(self.listafilename.keys()[i]) + '.html')
                self.printer(self.listafilename.keys()[i])
            output = codecs.open(fileurlout + ".txt", 'w', 'utf-8')
            for i in range(len(self.listafilename.keys())):
                self.elaboratorequery(decode_html(self.listafilename.keys()[i]), query, output)
            output.close()
        for i in range(numeromassimo):
            self.printer(self.listafilename.keys()[i])

    def altroesecutore(self, flag, numeromassimo, waiting, fileout, query):
        if flag == 0:
            print("Start downloading from urls")
            for i in range(len(self.url.keys())):
                print("Waiting number " + str(i + 1) + " of " + str(numeromassimo))
                time.sleep(waiting)
                urllib.urlretrieve(self.url.keys()[i], str(self.listafilename.keys()[i]) + '.html')
                self.printer(self.listafilename.keys()[i])
            for i in range(len(fileout)):
                output = codecs.open(fileout.keys()[i] + "_changed.txt", 'w', 'utf-8')
                self.elaboratorequery(decode_html(self.listafilename.keys()[i]), query, output)
                output.close()
        for i in range(numeromassimo):
            self.printer(self.listafilename.keys()[i])


def decode_html(nome):
    html_string = file(str(nome) + '.html').read()
    converted = BeautifulSoup.UnicodeDammit(html_string, isHTML=True)
    if not converted.unicode:
        print("Errore conversione unicode")
        return ''
    return converted.unicode


def main():
    listaurl = {}
    listanomi = {}

    for i in range(NUMERORISULTATI):
        listaurl[GOOGLEURL + str(i * 10)] = "inserito"
        listanomi["pagine_di_ricerca_" + str(i)] = "inserito"
    appoggio = ElaboratoreRicerca(listaurl, listanomi)
    appoggio.googleesecutore(CERCAINGOOGLE, NUMERORISULTATI, WAITINGTIME, FILEURL, QUERYGOOGLE)

    appoggio = open(FILEURL + ".txt", 'r')
    appoggio = appoggio.readlines()

    listaurl = {}
    for url in appoggio:
        if url.split('/search')[0] != '' and url != "":
            url = url.split("/url?q=")[1]
            listaurl[url.split('&sa=')[0]] = "inserito"

    listanomi = {}
    for i in range(len(listaurl)):
        listanomi["risultati_" + str(i)] = "inserito"

    appoggio = ElaboratoreRicerca(listaurl, listanomi)
    appoggio.altroesecutore(CERCAINRESULT, len(listaurl), 0, listanomi, QUERYSITO)

    num = len(listanomi)
    listanomi = {}
    for i in range(num):
        listanomi["risultati_" + str(i) + "_changed"] = "inserito"

    diz = {}
    Contaparole(listanomi, diz).printer("output.txt")

# Esecutore intero progetto
if __name__ == "__main__":
    main()