func = open("lessons.txt", 'r')
string = func.readlines()
data = []
j = 0
lessons = {}
inform = 0
phys = 0
cul = 0
for i in range(0, len(string)):
    string[i] = string[i].split()
    for j in range(0, len(string[i])):
        string[i][j] = string[i][j].split('(')
        for k in range(0, len(string[i][j])):
            string[i][j][k] = string[i][j][k].split()
            for l in range(0, len(string[i][j][k])):
                if string[i][j][k][l].isdigit():
                    string[i][j][k] = int(string[i][j][k][l])
                    if i == 0:
                        inform += string[i][j][k]
                    elif i == 1:
                        phys += string[i][j][k]
                    elif i == 2:
                        cul += string[i][j][k]
        print(string)
lessons["informatics"] = inform
lessons["physics"] = phys
lessons["physical_culture"] = cul
print(lessons)

# как это можно было оптимальнее сделать?
