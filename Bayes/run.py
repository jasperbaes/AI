#!/usr/bin/env python 
import train_data as data
import math

def checkInput():
    return len(data.o1) == len(data.o2) == len(data.o3) == len(data.o4)

def calc_chance(val_true, len, o1, o2, o3, o4):
    return (val_true/len) * (o1/val_true) * (o2/val_true) * (o3/val_true) * (o4/val_true)

def stats_res():
    count = 0
    for val in data.res:
        if (val == 1):
            count += 1
    return count

def calc_amount(array, r, type):
    count = 0
    for index, val in enumerate(array):
        if (data.res[index] == type and val == r):
            count += 1
    return count


if (not checkInput()):
    print("Woops, the input is not correct")
else:
    print("Calculating...")

    data.res1 = calc_chance(
        calc_amount(data.res, 1, 1),
        len(data.res),
        calc_amount(data.o1, data.r1, 1),
        calc_amount(data.o2, data.r2, 1),
        calc_amount(data.o3, data.r3, 1),
        calc_amount(data.o4, data.r4, 1)
    )

    data.res2 = calc_chance(
        calc_amount(data.res, 0, 0),
        len(data.res),
        calc_amount(data.o1, data.r1, 0),
        calc_amount(data.o2, data.r2, 0),
        calc_amount(data.o3, data.r3, 0),
        calc_amount(data.o4, data.r4, 0)
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