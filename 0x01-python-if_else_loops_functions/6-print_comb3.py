#!/usr/bin/python3

for x in range(10):
    for y in range(10):
        if y != x:
            if x < y:
                if x == 8 and y == 9:
                    print("{}{}".format(x, y))
                else:
                    print("{}{}".format(x, y), end=', ')
