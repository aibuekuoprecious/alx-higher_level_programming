#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    print_num = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            printr_num += 1
        except IndexError:
            break
    print()
    return print_num

