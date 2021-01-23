from random import randint

li = []
j=0
l = [randint(0, 50) for x in range(0, 50)]
print(l)

for i in range(0, len(l)):
    for j in range(i+1,len(l)):
        if l[i] == l[j]:
            break
    else:
        li.append(l[i])
print(li)