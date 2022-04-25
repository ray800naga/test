import re

pi_str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
pi_str = pi_str.replace(',', '')
pi_str = pi_str.replace('.', '')
splitted_str = pi_str.split()
print(splitted_str)
str_len_list = [len(i) for i in splitted_str]
print(str_len_list)