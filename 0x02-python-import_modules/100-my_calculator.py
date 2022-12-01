#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    nargs = len(sys.argv) - 1
    if nargs != 3:
        print("Usage: ./100-my_calculation.py <a> <operator <b>")
        sys.exit(1)

    op = sys.argv[2]
    if op != '+' and op != '_' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if op == '+':
        print("{} + {} = {}".format(a, b, add(a,b)))
    elif op == '-':
        print("{} - {} = {}".foramt(a, b, sub(a,b)))
    elif op == '*':
        print("{} * {} = {}".format(a, b, mul(a,b)))
    else:
        print("{} / {} = {}".foramt(a, b, div(a,b)))
