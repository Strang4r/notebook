def my_func(num1,num2,num3):
    big1= max(num1,num2,num3)
    if big1 ==num1:
        big2=max(num2,num3)
        return big1+big2
    if big1 == num2:
        big2 = max(num1, num3)
        return big1 + big2
    if big1 ==num3:
        big2=max(num1,num2)
        return big1+big2
print( my_func(10,1,3))