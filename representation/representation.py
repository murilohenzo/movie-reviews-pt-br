from gensim.models import TfidfModel
from gensim.corpora import Dictionary
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import numpy as np


class Representation(object):

    def repres_tfidf_with_skl(corpus):
        vector = TfidfVectorizer(sublinear_tf=True, max_features=1500)
        X = vector.fit_transform(corpus)
        X_col = vector.get_feature_names()
        return X, X_col

    def repres_tfidf(corpus_tokens):
        dictionary = Dictionary(corpus_tokens)
        doc_term_matrix = [dictionary.doc2bow(doc, allow_update=True) for doc in corpus_tokens]
        tfidf = TfidfModel(doc_term_matrix)
        tfidf_bow_repre = tfidf[doc_term_matrix]
        return tfidf_bow_repre, dictionary

    def represent_tfidf_bow_with_dictionary(tfidf_bow, dictionary):
        all_tfidf_rep = []
        for line in tfidf_bow:
            tfidf_rep = [0] * len(dictionary)
            for i, j in line:
                tfidf_rep[i] = j
            all_tfidf_rep.append(tfidf_rep)
        return np.asarray(all_tfidf_rep)
