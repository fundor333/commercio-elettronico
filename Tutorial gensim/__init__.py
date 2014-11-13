__author__ = 'Fundor333'

import Queue
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora, models, similarities

corpus = [[(0, 1.0), (1, 1.0), (2, 1.0)],[(2, 1.0), (3, 1.0), (4, 1.0), (5, 1.0), (6, 1.0), (8, 1.0)],[(1, 1.0), (3, 1.0), (4, 1.0), (7, 1.0)],[(0, 1.0), (4, 2.0), (7, 1.0)],[(3, 1.0), (5, 1.0), (6, 1.0)],[(9, 1.0)],[(9, 1.0), (10, 1.0)],[(9, 1.0), (10, 1.0), (11, 1.0)],[(8, 1.0), (10, 1.0), (11, 1.0)]]

tfidf = models.TfidfModel(corpus)

vec = [(0, 1), (4, 1)]

print(tfidf[vec])[(0, 0.8075244), (4, 0.5898342)]

index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=12)