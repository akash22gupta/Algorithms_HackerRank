#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    string = 'abcdefghijklmnopqrstuvwxyz'
    d = {}
    c=1
    for i in string:
        d[i] = c
        c+=1
    m = 0
    for i in word:
        if h[d[i]-1] > m:
            m = h[d[i]-1]
    return len(word)*m


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
