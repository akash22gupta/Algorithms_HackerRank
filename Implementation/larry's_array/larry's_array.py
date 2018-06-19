#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the larrysArray function below.
def larrysArray(a):
    n = 0
    for i in range(1,len(a)):
        j = i-1
        n += a[i]-1

        while(j>=0):
            if a[i]>a[j]:
                n -=1
            j -=1
        print(n)
    if n % 2 ==0:
        return("YES")
    else:
        return("NO")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
