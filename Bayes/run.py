#!/usr/bin/env python
import sys
sys.path.insert(0, './training_data')
import train_data2 as data
import math

LEN_INPUT = len(data.o)


def validInput():
    # Checks if the training data arrays have the same length
    # Checks if the result array has the correct length
    len_input = len(data.o[0])
    for arr in data.o:
        if (len(arr) != len(data.o[0])):
            return False
    if (LEN_INPUT-1 != len(data.r)):
        return False
    return True


def calc_chance(val_true, len, options):
    # Calculates the probability that the result is True or False
    if (val_true == 0):
        return 0  # not accurate (m-prediction would be better)
    res = val_true/len
    for option in options:
        res *= (option/val_true)
    return res


def calc_amount(array, r, type):
    # Returns the amount of True/False values where the result is True/False
    count = 0
    for index, val in enumerate(array):
        if (data.o[LEN_INPUT-1][index] == type and val == r):
            count += 1
    return count


def calc_options(state):
    # Returns an array with the amounts of each option
    options = []
    for x in range(LEN_INPUT-1):
        options.append(calc_amount(data.o[x], data.r[x], state))
    return options


def calc_percentage_true(res1, res2):
    return res1 / (res1 + res2) * 100 if res1 < res2 else res2 / (res1 + res2) * 100


def output(res1, res2):
    # print(" {0} vs {1}".format(round(res1, 4), round(res2, 4)))
    # times_bigger = res1/res2 if res1 > res2 else res2/res1
    # print(" The chance of {0} is {1} times bigger then {2} ".format(res1 > res2, round(times_bigger, 2), res1 < res2))

    chance_true = calc_percentage_true(res1, res2)
    chance_false = 100 - chance_true
    print("Prediction for {0}".format(data.r))
    print(" True / Yes  :  {0}%".format(round(chance_true, 2)))
    print(" False / No  :  {0}%".format(round(chance_false, 2)))


def init():
    if (not validInput()):
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


if (__name__ == "__main__"):
    init()
