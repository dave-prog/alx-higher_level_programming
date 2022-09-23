#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    list = dir(hidden_4)
    n = len(list)

    for i in range(2, n):
        result = list[i]
        if "__" not in result:
            print("{}".format(result))
