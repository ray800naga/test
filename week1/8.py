string = "Hi He Lead Because Boron Could Not Oxidize Flourine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
word_list = string.split()
element_dict = dict()
for i, word in enumerate(word_list, 1):
    if(i == 1 or (5 <= i and i <= 9) or i == 15 or i == 16 or i == 19):
        element_dict[word[0:1]] = i
    else:
        element_dict[word[0:2]] = i
print(element_dict)