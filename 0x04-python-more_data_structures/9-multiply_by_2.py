#!/usr/bin/python3
def multiply_by_2(my_dict):
    updated_dict = {}
    for key, value in my_dict.items():
        updated_dict[key] = value * 2
    return updated_dict
