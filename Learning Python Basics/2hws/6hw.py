l = []
i = 1
while True:
    l.append(
        ((i),dict({
            "название": input("введите название "),
            "цена": int(input("введиет цену")),
            "количество":int(input("введите количество")),
            "ед":str(input("введите единицы измерения"))
        }))
    )
    if input("товар добавленю добавить еще? (да/нет)")=="нет":
        break
    i+=1
print(f'список товаров:{l}')

di=l
for product in l:
    for key,value in product[-1].items():
        if key in di:
            if value not in di.get(key):
                di.get(key).append(value)
        else:
            di.update({key:[value]})

print(f"аналитика: {di}")
#знаю, схалтурил и подсмотрел решение, но постарался разобраться :)
#таки не понял кстати что за функция product и для чего она нужна
