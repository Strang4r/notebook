func = open("hr.txt", "r")
strings = func.readlines()
num = []
amount = len(strings)
for i in range(0, len(strings)):
    words = strings[i].split()
    words[1] = int(words[1])
    num.append(words[1])
    for j in range(0, len(words)):
        if words[1] < 20000:
            print(words[0])
            break
print("средняя зп= ", sum(num) / amount)
func.close()
