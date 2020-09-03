#!/usr/bin/python3
def uppercase(str):
    for i in str:
        upper = ord(i)
        if ord(i) >= 97 and ord(i) < 123:
            upper -= 32
        print("{}".format(chr(upper)), end="")
    print()
