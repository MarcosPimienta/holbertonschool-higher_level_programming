#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = 0
    if len(sys.argv) == 1:
        print("{}".format((len(sys.argv) - 1)))
    elif len(sys.argv) >= 3:
        for i in range(1, len(sys.argv)):
            num = num + int(sys.argv[i])
        print("{}".format(num))
