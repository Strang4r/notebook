en = int(input("Введи сколько сейчас энергии есть "))
cost = int(input("Введи стоимость за заход "))
delay = int(input("Введи интервал задежки в секундах "))

delta_en = delay // 180
delta_t = 0
delta_en_by_circle = int(en // (cost - delta_en))
for i in range(0, delta_en_by_circle):
    if en < cost:
        print("not enough energy")
        break
    else:
        en -= 16
        en = en + delta_en
        delta_t += delay // 60
        if delta_t > 60:
            print(
                f"\n прошло {round(delta_t // 60)} часов,{delta_t % 60} минут после запуска, заходов выполнено {i+1}, энергии осталось {en}")
        else:
            print(f"\n прошло {delta_t} минут после запуска, заходов выполнено {i+1}, энергии осталось {en}")
