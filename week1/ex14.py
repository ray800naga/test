import numpy as np

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
    for doc in docs:
        if(term in doc):
            num += 1
    return (np.log10(len(docs) / num) + 1)

docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]
for term in terms:
    print("idf({}) = {}".format(term, idf(term, docs)))
