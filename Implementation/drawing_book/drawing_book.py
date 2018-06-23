#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if (n%2)!=0:
        n = n-1
    if (p%2)!=0:
        p = p-1
    r1 = int(abs((n-p))/2)
    r2 = int(abs((0-p))/2)
    if r1 > r2:
        return r2
    else:
        return r1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
