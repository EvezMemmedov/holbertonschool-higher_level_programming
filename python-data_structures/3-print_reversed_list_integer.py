#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = len(my_list) - 1
    temp = []
    for i in my_list:
        temp = my_list[a]
        a = a - 1
        print("{:d}".format(temp))
