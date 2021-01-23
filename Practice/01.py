def some_func(array, operation):
    for i in range(0, len(array) - 1):
        if operation == "AND":
            if array[i] == array[i + 1]:
                s = True
            else:
                s = False
        if operation == "OR":
            if array[i] | array[i + 1]:
                s = True
            else:
                s = False
        if operation == "XOR":
            if array[i] ^ array[i + 1]:
                s = False
            else:
                s = True

    return s


l = some_func([True, True, False], "XOR")
print(l)
