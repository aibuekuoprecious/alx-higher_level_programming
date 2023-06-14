#!/usr/bin/python3
def simple_delete(my_dict, key=""):
    updated_dict = my_dict.copy()
    if key in updated_dict:
        del updated_dict[key]
    return updated_dict
