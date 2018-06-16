#!/bin/python3

import math
import os
import random
import re
import sys
d ={}
dd={}
def cal_count(l):
    if l not in d:
        dd[l] = 0
        return 0
    count =1
    count1= 1
    for i in d[l]:
        count += 1
        # print("i=%s,count=%s"%(i,count))
        count+=cal_count(i)
    return (count-count1)


if __name__ == '__main__':
    tree_nodes, tree_edges = map(int, input().split())
    count = 0
    tree_from = [0] * tree_edges
    tree_to = [0] * tree_edges
    for i in range(tree_edges):
        tree_from[i], tree_to[i] = map(int, input().split())
        if tree_to[i] not in d:
            d[tree_to[i]] = [tree_from[i]]
        else:
            d[tree_to[i]].append(tree_from[i])
    # print(d)
    for i in d:
        dd[i] = cal_count(i)
    # print(d)
    # print(dd)
    for i in dd:
        if dd[i]%2!=0 and i!=1:
            count+=1
    print(count)
