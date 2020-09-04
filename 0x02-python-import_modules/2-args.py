#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{} {}".format((len(sys.argv) - 1), "arguments."))
    elif len(sys.argv) == 2:
        print("{} {}".format((len(sys.argv) - 1), "argument:"))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} {}".format((len(sys.argv) - 1), "arguments:"))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
