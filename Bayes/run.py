#!/usr/bin/env python 
import train_data as data
import math

LEN_INPUT = len(data.o)

def checkInput():
    len_input = len(data.o[0])
    for arr in data.o:
        if (len(arr) != len(data.o[0])):
            return False
    if (LEN_INPUT-1 != len(data.r)):
        return False
    return True

def calc_chance(val_true, len, options):
    res = val_true/len
    for option in options:
        res *= (option/val_true)
    return res

def calc_amount(array, r, type):
    count = 0
    for index, val in enumerate(array):
        if (data.o[LEN_INPUT-1][index] == type and val == r):
            count += 1
    return count

def calc_options(state):
    options = []
    for x in range(LEN_INPUT-1):
        options.append(calc_amount(data.o[x], data.r[x], state))
    return options

def init():
    if (not checkInput()):
        print("Oops, the input is not correct")
    else:
        res1 = calc_chance(
            calc_amount(data.o[LEN_INPUT-1], 1, 1),
            len(data.o[LEN_INPUT-1]),
            calc_options(1)
        )

        res2 = calc_chance(
            calc_amount(data.o[LEN_INPUT-1], 0, 0),
            len(data.o[LEN_INPUT-1]),
            calc_options(0)
        )

        output(res1, res2)

def output(res1, res2):
    print("{0} vs {1}".format(round(res1, 4), round(res2, 4)))
    times_bigger = res1/res2 if res1 > res2 else res2/res1
    print("The chance of {0} is {1} times bigger then {2} ".format(res1 > res2, round(times_bigger, 2) , res1 < res2))
    
    if (res1 < res2):
        chance_true = 100/times_bigger
        chance_false = 100 - chance_true
    else:
        chance_false = 100/times_bigger
        chance_true = 100 - chance_false

    print("TRUE  :  {0}%".format(round(chance_true, 2)))
    print("FALSE :  {0}%".format(round(chance_false, 2)))


if (__name__ == "__main__"):
    init()