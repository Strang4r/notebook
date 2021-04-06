func=open("test_file.txt","r")
strings=func.readlines()
print(len(strings))
for i in range (0,len(strings)):
    words=strings[i].split()
    print(len(words))
    