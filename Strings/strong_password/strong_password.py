import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    res = 0
    n,l,u,s = 0,0,0,0
    for i in password:
        if i in numbers:
            n = 1
        if i in lower_case:
            l =1
        if i in upper_case:
            u =1
        if i in special_characters:
            s =1
    if n == 0:
        res +=1
    if u == 0:
        res +=1
    if l == 0:
        res +=1
    if s == 0:
        res +=1
    if len(password)<6:
        if (6 - len(password)) > res:
            return (6 - len(password))
        else:
            return res
    else:
        return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
