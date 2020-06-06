#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    firstlast =s.split(" ")
    first1 = firstlast[0]
    last1 = firstlast[1]

    if(first1[0].isalpha()):
        f1 = first1[0].upper()
    else :
        f1 = first1[0]
    f2 = first1[1:len(first1)]

    first = f1 +f2

    return first + " "

    if (last1[0].isalpha()):
        l1 = last1[0].upper()
    else:
        l1 = last1[0]
    l2 = last1[1:len(last1)]

    last = l1 + l2

    return last



if __name__ == '__main__':


    s = input()

    result = solve(s)

    print (result)