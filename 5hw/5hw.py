from random import randint

func = open('number_file.txt', "w")
for i in range(0, 10):
    content = [randint(0, 500) for x in range(0, 100)]
    for element in content:
        func.write(str(element))
        func.write(" ")
func.close()
func = open('number_file.txt', "r")
string = func.read()
string = string.split()
for i in range (0,len(string)):
    string[i]=int(string[i])
s=sum(string)
print(string)
print(s)
