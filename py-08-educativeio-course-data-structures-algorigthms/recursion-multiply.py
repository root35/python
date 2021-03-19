from math import pow

def multiply_iter(x, y):
    if x == 0 and y == 0:
        return 0

    product = 0
    tempx = x
    tempy = y
    i = 0

    while tempx != 0:
        last_digit_x = tempx % 10
        tempx = tempx // 10
        pos_x = pow(10, i) * last_digit_x

        tempy = y
        j = 0

        while tempy != 0:
            last_digit_y = tempy % 10
            tempy = tempy // 10
            product += pos_x * ((pow(10, j) * last_digit_y))
            j += 1

        i += 1

    return product


def multiply_rec(x, y):
    # This cuts down on the total number of
    # recursive calls:
    if x < y:
        return multiply_rec(y, x)
    if y == 0:
        return 0
    return x + multiply_rec(x, y-1)


def main():
    print(multiply_iter(15, 13))
    print(multiply_rec(15, 13))
    print(15*13)

if __name__ == '__main__':
    main()
