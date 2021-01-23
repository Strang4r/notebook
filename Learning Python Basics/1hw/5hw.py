income=int(input("введи доходы"))
spends=int(input("введи расходы"))
if income>spends:
    print("прибыль больше затрат!")
    rent=income/spends
    wrks=int(input("сколько человек работает в вашей фирме?"))
    eff=income/wrks
    print("рентабильность равна:", rent,"эффективность на работника равна:",eff)
elif income==spends :
    print("вышли в ноль")
elif income<spends:
    print("работаем в минус!")
