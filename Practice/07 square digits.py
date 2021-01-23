"""Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 9^2 is 81 and 1^2 is 1.

Note: The function accepts an integer and returns an integer"""
def square_digits(num):
    res=""
    for el in str(num):
        res+=str(int(el)**2)
    return int(res)

square_digits(9119)



# def square_digits(num):
#     res=""
#     num=str(num)
#     res = map(lambda el: str(int(el) ** 2), num)
#     res=str(map(lambda el: for el in num))
#
#     return res
#
# square_digits(9119)
# print(type(square_digits(9119)))
