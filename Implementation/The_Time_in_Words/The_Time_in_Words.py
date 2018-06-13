#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):

    d = {0:"zero",
       1: "one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine",
        10:"ten",
        11:"eleven",
        12:"twelve",
        13:"thirteen",
       14 :"fourteen",
       15 :"fifteen",
       16 :"sixteen",
       17 :"seventeen",
       18 :"eighteen",
       19 :"nineteen",
       20 :"twenty",
        21:"twenty one",
        22:"twenty two",
       23 :"twenty three",
        24:"twenty four",
       25 :"twenty five",
       26 :"twenty six",
        27:"twenty seven",
        28:"twenty eight",
       29 :"twenty nine"
    }

    if m ==0:
        return (d[h] + " o' clock")
    elif m<=30 and m>=1:
        if m == 15:
            return ('quarter past '+d[h])
        elif m==30:
            return ('half past '+d[h])
        if m == 1:
            return (d[m]+' minute past '+d[h])
        else:
            return (d[m]+' minutes past '+d[h])

    elif m>30:
        if h ==12:
            if m == 45:
                return ('quarter to one')
            else:
                return (d[60-m]+' minutes to one')
        if m == 45:
                return ('quarter to '+d[h+1])
        else:
            return (d[60-m]+' minutes to '+d[h+1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
