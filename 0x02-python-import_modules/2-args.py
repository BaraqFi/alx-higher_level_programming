#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = len(sys.argv) - 1
    if (argv == 0):
        print("0 arguments.")
    elif argv == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(argv))
        for n in range(1, argv + 1):
            print("{}: {}".format(n, sys.argv[n]))
