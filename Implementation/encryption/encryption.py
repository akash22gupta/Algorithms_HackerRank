#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    ss=''
    s = s.replace(" ","")
    l = len(s)
    st=math.sqrt(l)
    c=math.ceil(st)
    f=math.floor(st)
    if (c*f)<l:
        f=c
    for i in range(0,c):
        for j in range(i,l,c):
            if s[j]:
                ss+=s[j]
        ss+=' '
    return ss
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
