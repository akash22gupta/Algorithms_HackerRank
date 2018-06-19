#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # Write your code here.
    #
    new_grades = []
    for i in grades:
        if i % 5 >= 3:
            temp = (5-(i%5))+i
            if temp >= 40:
                new_grades.append(temp)
            else:
                new_grades.append(i)
        else:
            new_grades.append(i)
    return new_grades



if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
