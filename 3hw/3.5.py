def my_func(l):
    s = 0
    i = 0
    stop_ch="@"
    while stop_ch not in l:
        l=l.split()
        for i in range(0, len(l)):
            if l[i] == "@":
                break
            else:
                l[i] = int(l[i])
                s = s + l[i]
        print("сумма = ",s)
        l = input("Введите числа через пробел что бы сложить их. для выхода введите @")
    if stop_ch in l:
        l = l.split()
        for i in range(0, len(l)):
            if l[i] == "@":
                break
            else:
                l[i] = int(l[i])
                s = s + l[i]

    print("сумма = ",s)


my_func(input("Введите числа через пробел что бы сложить их. для выхода введите @"))

#  for co in range(0,len(l)):
#         if l[co]=="@":
#             break
#         else:
#             l[co]=int(l[co])
#     return l
#     print(l)
#     x=0
#     for i in range (0,len(l)):
#         x=x+l[i]
#         if l[i]=="@":
#             break
#         return l,x
