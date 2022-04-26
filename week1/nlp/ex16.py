import numpy as np

def cosine_sim(x1, x2):
    """calculate cosine similarity value
    :param x1: vector 1
    :type x1: np.ndarray
    :param x2: vector 2
    :type x2: np.ndarray
    :returns: cosine similarity value
    :rtype: float
    """
    return (np.dot(x1, x2) / (np.linalg.norm(x1) * np.linalg.norm(x2)))

if __name__ == '__main__':
    x1 = np.array([1, 0, 0, 1])
    x2 = np.array([0, 1, 0, 1])
    print("{:.1f}".format(cosine_sim(x1, x2)))