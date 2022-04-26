f = open('./dataset/data.txt', 'r', encoding='UTF-8')
#各行を格納するためのリストを初期化
line_list = list()
#各行について，改行文字を取り除いた形でline_listに格納
for i in f:
    line_list.append(i.replace('\n', ''))
#単語ごとに分割したリストを格納するためのリストを初期化
docs = list()
#各行について，「と」で分割した単語リストをdocsに格納
for i in line_list:
    docs.append(i.split('と'))
print("docs : ", end = '')
print(docs)
#果物の種類を格納するリストを初期化
terms = list()
#docsの各要素について，termsに入っていない場合は追加
for i in docs:
    for j in i:
        if j not in terms:
            terms.append(j)
        else:
            continue
print("terms: ", end = '')
print(terms)

