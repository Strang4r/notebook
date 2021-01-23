l=[]
n=int(input("введите количество "))
for i in range(0,n):
    el=int(input())
    l.append(el)

print(l)
i=0
while i<(n-1):
    l[i],l[i+1]=l[i+1],l[i]
    i+=2
print(l)