#!/usr/bin/python3

def safe_division(a, b):
    quotient = 0
    try:
        quotient = a / b
    except ZeroDivisionError:
        print("Division by 0")
    except TypeError:
        print("Wrong type")
    finally:
        return quotient

def list_division(my_list_1, my_list_2, list_length):
    result_li = []
    for i in range(list_length):
        try:
            result_li.append(safe_division(my_list_1[i], my_list_2[i]))
        except IndexError:
            print("Out of range")
            result_li.append(0)

    return result_li
