#!/usr/bin/python3
import sys
if __name__ == "__main__":
    for i in range(len(sys.argv)):
        if len(sys.argv) == 0:
            print("0 arguments.")
        else:
            print("{} argument:".format(i), end="")
            print("{}: {}".format(i, sys.argv[i]), end="")
