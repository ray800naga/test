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
    #nが負の時はエラーを返す
    if(n <= 0):
        print("invalid value.")
        return
    #n=2の時はbi-gramと表記
    if (n == 2):
        print("単語bi-gram: ", end = '')
    #その他のときはn-gramと表記
    else:
        print("単語" + str(n) + "-gram: ", end = '')
    #単語n-gramを格納するリストを初期化
    word_n_gram = list()
    #各n-gramの最初の単語に対応するindexは0~len(seq)-n
    for i in range(0, len(seq) - n + 1):
        #一時格納用のtmp_listを初期化
        tmp_list = list()
        #tmp_listにn単語分格納する
        for j in range(n):
            tmp_list.append(seq[i + j])
        #単語n-gramとして格納
        word_n_gram.append(tmp_list)
    print(word_n_gram)
    #n=2の時はbi-gramと表記
    if (n == 2):
        print("文字bi-gram: ", end = '')
    #その他のときはn-gramと表記
    else:
        print("文字" + str(n) + "-gram: ", end = '')
    #seqに入った文字列をすべて連結してjoined_strに格納
    joined_str = ''.join(seq)
    #文字n-gramを格納するリストを初期化
    char_n_gram = list()
    #文字n-gramの最初の文字に対応するindexは0~len(joined_str)-n
    for i in range(0, len(joined_str) - n + 1):
        #n文字分を文字n-gramとして格納
        char_n_gram.append(joined_str[i: i + n])
    print(char_n_gram)
    

args = sys.argv[1:]
n = int(input("n:"))
n_gram(n, args)
