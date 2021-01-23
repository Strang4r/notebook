from itertools import count, cycle

# c = int(input("введите число с которого начнется отсчет"))
# x=c*10
# nums = count(start=c, step=1)
# for i in range(c,x):
#
#     print(next(nums))


nums=[x for x in range(0,5)]
for i,c in enumerate(cycle(nums)):
    print(c)
    if i >25:
        break