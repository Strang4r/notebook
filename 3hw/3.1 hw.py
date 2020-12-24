def division(arg1, arg2):
    while arg2==0:
        print("Error! Division by zero")
        arg2=int(input("try again"))
    return arg1/arg2

calc =division(
    int(input("input first arg")),int(input("input second arg"))
)
print(calc)
#не совсем понял как правильно использовать try, exeption в обработке ошибок