l=[8,4,3,3,2]
x=int(input())
i=l[0]
c=0
for c in range(0,len(l)):
    if x>l[c]:
        l.insert(c,x)
        print(l)
    if len(l)>5:
        break
    if x<l[4]:
        l.append(x)
        print(l)