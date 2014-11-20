from requests import models

__author__ = 'Fundor333'

import linecache
import logging

from gensim import corpora,models

from primaconsegna import getfromgoogle, NUMERORISULTATI


LEXICONNAME = "./out/out.txt"
DICTIONARYNAME = './out/deerwester.dict'
CORPUSNAME = './out/deerwester.mm'


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
    return dictio, texts


def makecorpus(dictionary, texts):
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize(CORPUSNAME, corpus)  # store to disk, for later use
    return corpus


def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    dictio, texts = makedictionary()
    corpus = makecorpus(dictio, texts)
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    for doc in corpus_tfidf:
        print(doc)


if __name__ == "__main__":
    main()
