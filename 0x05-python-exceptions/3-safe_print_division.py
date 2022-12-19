#!/usr/bin/python3

def safe_print_division(a,b):
    quotient = 0
    try:
        quotient = a/b
    except ZeroDivisionError:
        quotient = None
    except TypeError:
        quotient = None
    finally:
        print('Inside result: {}'.format(quotient))
    return quotient
