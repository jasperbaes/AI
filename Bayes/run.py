#!/usr/bin/env python 
import math

# Training data
o1 = [1,0,0,1,0,0,1,0,1,1,0,0,1,0,0,0,0,0,1,0]
o2 = [0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1]
o3 = [0,0,1,1,0.5,0,0,0,0,1,0.5,0.5,0,1,0.5,0,0,0,1,0]
o4 = [1,0,0,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,0,1]
res = [1,0,0,1,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0]

# What we know
r1 = 1
r2 = 0
r3 = 1
r4 = 0

def checkInput():
    return len(o1) == len(o2) == len(o3) == len(o4)

def calc_change(val_true, len, o1, o2, o3, o4):
    return (val_true/len) * (o1/val_true) * (o2/val_true) * (o3/val_true) * (o4/val_true)

def stats_res():
    count = 0
    for val in res:
        if (val == 1):
            count += 1
    return count

def calc_amount(array, r, type):
    count = 0
    for index, val in enumerate(array):
        if (res[index] == type and val == r):
            count += 1
    return count


if (not checkInput()):
    print("Woops, the input is not correct")
else:
    print("Calculating...")

    res1 = calc_change(
        calc_amount(res, 1, 1),
        len(res),
        calc_amount(o1, r1, 1),
        calc_amount(o2, r2, 1),
        calc_amount(o3, r3, 1),
        calc_amount(o4, r4, 1)
    )

    res2 = calc_change(
        calc_amount(res, 0, 0),
        len(res),
        calc_amount(o1, r1, 0),
        calc_amount(o2, r2, 0),
        calc_amount(o3, r3, 0),
        calc_amount(o4, r4, 0)
    )

    print(round(res1, 4), round(res2, 4))

    print("The result is {0}".format(res1 > res2))


