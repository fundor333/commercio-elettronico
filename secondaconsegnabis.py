import linecache
import logging

from gensim import corpora

from primaconsegna import getfromgoogle, NUMERORISULTATI


__author__ = 'Fundor333'

LEXICONNAME = "./out/out.txt"
DICTIONARYNAME = './out/deerwester.dict'


def readlexicon():
    return linecache.getline(LEXICONNAME, 0)


def makedictionary():
    documents = []
    try:
        fistline = linecache.getline(LEXICONNAME, 1)
    except IOError:
        fistline = getfromgoogle(NUMERORISULTATI)
    for i in range(0, int(fistline)):
        filein = open("./out/" + str(i) + ".txt")
        for line in filein:
            documents.append(line)

    spamword = open("spamword.teo")
    stoplist = None
    for line in spamword:
        stoplist = set(line.split())
    texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]

    all_tokens = sum(texts, [])
    tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
    texts = [[word for word in text if word not in tokens_once] for text in texts]
    dictio = corpora.Dictionary(texts)
    dictio.save(DICTIONARYNAME)  # store the dictionary, for future reference
    return dictio


def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    dictelaborate = makedictionary()
    new_doc = "Human computer interaction"
    new_vec = dictelaborate.doc2bow(new_doc.lower().split())
    print(new_vec)


if __name__ == "__main__":
    main()
