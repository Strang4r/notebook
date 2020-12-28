from random import random, randint, randrange

l = [randint(0, 500) for x in range(20)]


def big_el():
    i = 0
    cnt = 1
    li = []
    for i in range(i, 20):
        if l[cnt] > l[i]:
            x = l[cnt]
            li.append(x)
        cnt += 1
        if cnt == 14:
            break

    print(li)
    return li


print(l)
print(big_el())
