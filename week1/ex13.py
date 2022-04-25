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

docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]
for doc in docs:
    for term in terms:
        print("tf({}, {}) = {:.1f}".format(term, doc, tf(term, doc)), end = ' ')
    print()