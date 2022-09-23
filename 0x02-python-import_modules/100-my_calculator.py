#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    args = sys.argv
    n = len(args)

    if n != 4:
        print("Usage: {} <a> <operator> <b>".format(args[0]))
        exit(1)

    a = int(args[1])
    b = int(args[3])
    op = args[2]

    if op == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
        exit(0)
    elif op == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
        exit(0)
    elif op == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
        exit(0)
    elif op == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
