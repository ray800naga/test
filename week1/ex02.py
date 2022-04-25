for i in range(1, 31):
    flag = 0
    if (i % 3 == 0):
        print("Fizz", end = '')
        flag = 1
    if (i % 5 == 0):
        print("Buzz", end = '')
        flag = 1
    if (flag == 0):
        print(i, end = '')
    print()
    