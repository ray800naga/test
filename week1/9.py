import sys
import copy
import random

#コマンドライン引数の取得
args = sys.argv
#コマンドライン引数の0番目は除外
word_list = args[1:]
#入れ替えた文字列を格納するためのリストを初期化
new_list = list()
for i, word in enumerate(word_list):
    #3文字以下の場合は入れ替えがないので，そのままnew_listに格納
    if(len(word) <= 3):
        new_list.append(word)
        continue
    #文字の入れ替えを行うために，いったん文字列をリスト化してnew_listに格納
    new_list.append(list(word))
    #1~len(word)-2の数をランダムに並べ替えたものをrandom_num_listに格納
    random_num_list = random.sample(range(1, len(word) - 1), len(word) - 2)
    for j in range(1, len(word) - 1):
        #両端以外の文字をランダムに並び変える
        new_list[i][j] = word[random_num_list[j - 1]]
    #リスト化した文字列をstr型に戻す
    new_list[i] = ''.join(new_list[i])
#単語のリストを文字列化して出力
print(' '.join(new_list))