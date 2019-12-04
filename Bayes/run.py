#!/usr/bin/env python 
import train_data as data
import math

LEN_INPUT = len(data.o)

def checkInput():
    len_input = len(data.o[0])
    for arr in data.o:
        if (len(arr) != len(data.o[0])):
            return False
    return True

def calc_chance(val_true, len, o1, o2, o3, o4):
    return (val_true/len) * (o1/val_true) * (o2/val_true) * (o3/val_true) * (o4/val_true)

def calc_amount(array, r, type):
    count = 0
    for index, val in enumerate(array):
        if (data.o[LEN_INPUT-1][index] == type and val == r):
            count += 1
    print(count)
    return count


if (not checkInput()):
    print("Woops, the input is not correct")
else:
    print("Calculating...")

    data.res1 = calc_chance(
        calc_amount(data.o[LEN_INPUT-1], 1, 1),
        len(data.o[LEN_INPUT-1]),
        calc_amount(data.o[0], data.r[0], 1),
        calc_amount(data.o[1], data.r[1], 1),
        calc_amount(data.o[2], data.r[2], 1),
        calc_amount(data.o[3], data.r[3], 1)
    )

    data.res2 = calc_chance(
        calc_amount(data.o[LEN_INPUT-1], 0, 0),
        len(data.o[LEN_INPUT-1]),
        calc_amount(data.o[0], data.r[0], 0),
        calc_amount(data.o[1], data.r[1], 0),
        calc_amount(data.o[2], data.r[2], 0),
        calc_amount(data.o[3], data.r[3], 0)
    )

    print("{0} vs {1}".format(round(data.res1, 4), round(data.res2, 4)))
    print("The chance of {0} is {1} times bigger then {2} ".format(data.res1 > data.res2, round(data.res1/data.res2 if data.res1 > data.res2 else data.res2/data.res1, 2) , data.res1 < data.res2))
    times_bigger = data.res1/data.res2 if data.res1 > data.res2 else data.res2/data.res1

    if (data.res1 < data.res2):
        chance_true = 100/times_bigger
        chance_false = 100 - chance_true
    else:
        chance_false = 100/times_bigger
        chance_true = 100 - chance_false

    print("TRUE  :  {0}%".format(round(chance_true, 2)))
    print("FALSE :  {0}%".format(round(chance_false, 2)))