#через list
wi = [12, 1, 2]
sp = [3, 4, 5]
su = [6, 7, 8]
au = [9, 10, 11]
sns = [wi, sp, su, au]
month = int(input('month number?'))
a = 0
for i in range(0, 3):
    for c in range(0, 2):
        if month == sns[i][c]:
            if i == 0:
                print('winter')
            if i == 1:
                print('spring')
            if i == 2:
                print('summer')
            if i == 3:
                print('autumn')

# через dict
# seasons = {"12": "winter", "1": 'winter', "2": 'winter',
#            "3": 'spring', "4": 'spring', "5": 'spring',
#            "6": 'summer', "7": 'summer', "8": 'summer',
#            "9": 'autumn', "10": 'autumn', "11": 'autumn'}
# month = input('month number?')
# print(seasons[month])
