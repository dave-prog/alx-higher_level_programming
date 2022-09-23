#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    args = sys.argv
    n = len(args)

    result = 0

    for i in range(1, n):
        result += int(args[i])
    print("{}".format(result))
