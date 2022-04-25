f = open('./dataset/data.txt', 'r', encoding='UTF-8')
#各行を格納するためのリストを初期化
line_list = list()
#各行について，改行文字を取り除いた形でline_listに格納
for i in f:
    line_list.append(i.replace('\n', ''))
#単語ごとに分割したリストを格納するためのリストを初期化
word_split_list = list()
#各行について，「と」で分割した単語リストをword_split_listに格納
for i in line_list:
    word_split_list.append(i.split('と'))
print("docs : ", end = '')
print(word_split_list)
#果物の種類を格納するリストを初期化
terms_list = list()
#word_split_listの各要素について，terms_listに入っていない場合は追加
for i in word_split_list:
    for j in i:
        if j not in terms_list:
            terms_list.append(j)
        else:
            continue
print("terms: ", end = '')
print(terms_list)