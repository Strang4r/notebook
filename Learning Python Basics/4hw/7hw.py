def fact(n):
    f = 1
    for i in range(1, n):
        f = f * i
        yield f


n = int(input("введите до скольки посчитать факториал"))
for el in fact(n):
    print(el)
