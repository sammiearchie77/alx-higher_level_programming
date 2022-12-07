#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None:
        new_dict = a_dictionary
        new_dict[key] = value
        return new_dict
