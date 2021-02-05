def function1(x1, x2):
    return x1 + x2


def function2(x1, x2):
    return x1 * x2


# This is a comment
def function3(x1):
    for x in x1:
        print('hello there {0}'.format(x))


def main():
    foo = function1(5, 2)
    print(foo)


if __name__ == '__main__':
    main()
