word = ["cat","window","defebestrate"]


# for i in word:
#     print(i,len(i))


word_2 = [i for i in word if len(i) != 3]
print(word_2)