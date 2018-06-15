#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#

def findFactor(a):
    l = []
    for i in range(1,(a//2)+1):
        if a%i==0:
            l.append(i)
    l.append(a)
    return l

def isFactor(i,a):
    for item in a:
        if i%item != 0:
            return 'NO'
    return 'YES'

def getTotalX(a, b):
    #
    # Write your code here.
    #
    l=[]
    count = 0
    for item in b:
        l.append(findFactor(item))
    l = list(set(l[0]).intersection(*l))

    for item in l:
        result = isFactor(item,a)
        if result == 'YES':
            count += 1
    return (count)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
