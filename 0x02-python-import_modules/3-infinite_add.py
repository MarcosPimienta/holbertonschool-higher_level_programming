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
    #     print("{} {}".format((len(sys.argv) - 1), "argument:"))
    #     print("{}: {}".format(1, sys.argv[1]))
    # else:
    #     print("{} {}".format((len(sys.argv) - 1), "arguments:"))
