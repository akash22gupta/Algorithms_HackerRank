#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    j = n-1
    x=[]
    k = arr[n-1]
    while j >0:
        flag = 0
        if arr[j-1] >k:
            arr[j]=arr[j-1]
            flag = 1
        if flag ==0:
            break
        print(" ".join(map(str,arr)))
        j-=1
    arr[j]=k
    print(" ".join(map(str,arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
