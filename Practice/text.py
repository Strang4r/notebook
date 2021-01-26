# def alphabet_position(text):
#     i = 0
#     for i in range(len(string.ascii_lowercase)):
#         z = str(" ".join([x for x in text.lower() if x == list[string.ascii_lowercase[i]]]))
#         print(z)
#
#
# alphabet_position("sometext")
# c = 1
import string

x = "abc"
i = 0
c=string.ascii_lowercase[i]
for z in x:
    for i in range(len(string.ascii_lowercase)):
        print(x,c)
# if x == string.ascii_lowercase[i]:
#     print(string.ascii_lowercase[i])

