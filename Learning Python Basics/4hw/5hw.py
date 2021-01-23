from functools import reduce

l=[x for x in range(100,1001) if x % 2 ==0]
prod= reduce(lambda x,y: x*y,l)
print(l)
print(prod)