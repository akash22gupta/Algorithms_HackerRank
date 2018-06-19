#!/bin/python3

import os
import sys

#
# Complete the breakingRecords function below.
#
def breakingRecords(scores):
    #
    # Write your code here.
    #
    l = scores[0]
    lcount = 0
    hcount = 0
    h = scores[0]
    for score in scores:
        if score > h:
            hcount += 1
            h = score
        if score < l:
            lcount += 1
            l = score
    return(hcount,lcount)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    score = list(map(int, input().rstrip().split()))

    result = breakingRecords(score)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()
