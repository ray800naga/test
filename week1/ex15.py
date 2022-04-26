import numpy as np

def tf(term, doc):
    """calculate tf value
    :param term: term used in docs
    :type term: str
    :param doc: document
    :type doc: list
    :returns: tf value
    :rtype: float
    """
    return(doc.count(term) / len(doc))

def idf(term, docs):
    """calculate idf value
    :param term: term used in docs
    :type term: str
    :param docs: list of document
    :type docs: list
    :returns: idf value
    :rtype: float
    """
    num = 0
    #docsの中にtermがいくつあるのかをカウントする．
    for doc in docs:
        if(term in doc):
            num += 1
    return (np.log10(len(docs) / num) + 1)

def tf_idf(terms, docs):
    """calculate tf-idf value
    :param terms: list of terms used in docs
    :type terms: list
    :param docs: list of documents
    :type docs: list
    :returns: tf-idf values matrix
    :rtype: numpy.ndarray
    """
    mtx = np.zeros((len(docs), len(terms)))
    for i, doc in enumerate(docs):
        for j, term in enumerate(terms):
            mtx[i][j] = tf(term, doc) * idf(term, docs)
    return (mtx)

docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]
print(tf_idf(terms, docs))