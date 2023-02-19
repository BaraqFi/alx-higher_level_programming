#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argv = len(sys.argv) - 1
    if argv < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv == 3:
        opp = sys.argv[2]
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[3])
        if opp == '+':
            print("{} + {} = {}".format(num1, num2, add(num1, num2)))
        elif opp == '-':
            print("{} - {} = {}".format(num1, num2, sub(num1, num2)))
        elif opp == '*':
            print("{} * {} = {}".format(num1, num2, mul(num1, num2)))
        elif opp == '/':
            print("{} / {} = {}".format(num1, num2, div(num1, num2)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
