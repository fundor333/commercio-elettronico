__author__ = 'Fundor333'

import linecache

from gensim import corpora, models, similarities

from primaconsegna import getfromgoogle, NUMERORISULTATI


LEXICONNAME = "./out/out.txt"
DICTIONARYNAME = './out/deerwester.dict'
CORPUSNAME = './out/deerwester.mm'
LSINAME = './out/model.lsi'
INDEXNAME = "./out/deerwester.index"
COLDSTARTNAME = "./out/coldstartbis.txt"
WARMSTARTNAME = "./out/warmstartbis.txt"


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
    dictio.save(DICTIONARYNAME)
    return dictio, texts


def makecorpus(dictionary, texts):
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize(CORPUSNAME, corpus)
    return corpus


def makelsi(corpus, dictionary):
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2)
    lsi.save(LSINAME)
    return models.LsiModel.load(LSINAME)


def startprinter(dictionary, doc, corpus, namefile):
    lsi = makelsi(corpus, dictionary)
    index = similarities.MatrixSimilarity(lsi[corpus])
    vec_bow = dictionary.doc2bow(doc.lower().split())
    vec_lsi = lsi[vec_bow]
    sims = index[vec_lsi]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    startout = open(namefile, 'w')
    for enupla in sims:
        startout.write(str(enupla) + '\n')


def main():
    dictionary, texts = makedictionary()
    corpus = makecorpus(dictionary, texts)
    # Cold Start
    print("Cold Start")
    outfile = open("./out/0.txt")
    doc = ""
    for riga in outfile:
        doc += riga
    startprinter(dictionary, doc, corpus, COLDSTARTNAME)
    # Warm Start
    print("Warm Start")
    doc = ""
    for num in range(19, 40):
        outfile = open("./out/" + str(num) + ".txt")
        for riga in outfile:
            doc += riga
    startprinter(dictionary, doc, corpus, WARMSTARTNAME)


if __name__ == "__main__":
    main()
