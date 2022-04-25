f = open('./dataset/data.txt', 'r', encoding = "UTF-8")
for i in f:
    print(i.replace('\n', ''))