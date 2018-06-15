#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    count = 0
    # Complete this function
    # if abs(x1-v1)<=abs(x2-v2):
    #         return "NO"
    k1=x1+v1
    k2=x2+v2
    if k1==k2 and (v1!=0 and v2!=0):
        return "YES"
    while(k1<k2 and count<10000):
        count +=1
        k1=k1+v1
        k2=k2+v2
        if k1 == k2:
            return "YES"
    return "NO"



x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
