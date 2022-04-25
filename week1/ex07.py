pi_str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
pi_str = pi_str.replace(',', '')    #, 除去
pi_str = pi_str.replace('.', '')    #. 除去
split_str = pi_str.split()
#print(split_str)    #単語ごとに分割したリストを表示
str_len_list = [len(i) for i in split_str]
print(str_len_list)