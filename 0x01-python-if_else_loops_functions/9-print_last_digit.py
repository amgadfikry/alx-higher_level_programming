def print_last_digit(number):
    num = number / 10
    temp = int(num) * 10
    res = number - temp
    if (res < 0):
        res *= -1
    print("{}".format(res), end="")
    return res
