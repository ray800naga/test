pi_str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
pi_str = pi_str.replace(',', '')    #, 除去
pi_str = pi_str.replace('.', '')    #. 除去
splitted_str = pi_str.split()
#print(splitted_str)    #単語ごとに分割したリストを表示
str_len_list = [len(i) for i in splitted_str]
print(str_len_list)