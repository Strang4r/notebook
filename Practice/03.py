'''Отсортируйте словарь по значению в порядке возрастания и убывания.'''
import operator

d = {
    "val1": 9,
    "val2": 3,
    "val3": 5,
    "val4": 4,
    "val5": 8
}

result = dict(sorted(d.items(), key=operator.itemgetter(0)))

print(result)
c = 1
