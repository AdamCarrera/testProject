def function1(x1, x2):
    return x1 + x2


def function2(x1, x2):
    return x1 / x2


# This is a different comment
def function3(x1):
    return 5 * x1


# This is another comment, on a different line
def function4(x1):
    print(x1)
    return x1 - 5


def main():
    foo = 3
    c = function4(foo)
    print(c)


if __name__ == '__main__':
    main()
