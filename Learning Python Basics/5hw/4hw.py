func = open("numbers.txt", 'r')
string = func.readlines()
new_num = []
c = ["один", "два", "три", "четыре"]
j = 0
fnc=open("new_numbers.txt","w")
for i in range(0, len(string)):
    nums = string[i].split()
    nums[0] = c[j]
    new_num.append(nums)
    content = " ".join(nums)+"\n"
    fnc.writelines(content)
    j += 1


