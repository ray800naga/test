import sys

def n_gram(n, seq):
    """print word n_gram and character n_gram
    
    :param n: specify n of "n-gram"
    :type n: int
    :param seq: sequence to input
    :type seq: list
    :returns: None
    :rtype: void
    """
    if(n <= 0):
        print("invalid value.")
        return
    if (n == 2):
        print("単語bi-gram: ", end = '')
    else:
        print("単語" + str(n) + "-gram: ", end = '')
    word_n_gram = list()
    for i in range(0, len(seq) - n + 1):
        tmp_list = list()
        for j in range(n):
            tmp_list.append(seq[i + j])
        word_n_gram.append(tmp_list)
    print(word_n_gram)
    if (n == 2):
        print("文字bi-gram: ", end = '')
    else:
        print("文字" + str(n) + "-gram: ", end = '')
    joined_str = ''.join(seq)
    char_n_gram = list()
    for i in range(0, len(joined_str) - n + 1):
        char_n_gram.append(joined_str[i: i + n])
    print(char_n_gram)
    

args = sys.argv[1:]
n = int(input("n:"))
n_gram(n, args)
