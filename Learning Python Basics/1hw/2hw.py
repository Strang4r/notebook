sec=int(input("input sec\n"))
h=sec // 3600
m=sec//60-h*60
s=sec-3600*h-m*60
print(" time h: %02d m: %02d s: %02d"% (h, m, s))
