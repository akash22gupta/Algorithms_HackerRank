#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(ar):
    d ={}
    for i in ar:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    d = dict(sorted(d.items(),key = lambda x :x[0]))
    max =0
    for i in d:
        if d[i]>max:
            max = d[i]
            res = i
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = migratoryBirds(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
