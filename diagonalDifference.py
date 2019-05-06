#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    l2r_element = []
    r2l_element = []
    sizeOfMat = len(arr)
    for i in range(len(arr)):
        l2r_element.append(arr[i][i])
        r2l_element.append(arr[i][sizeOfMat-1])
        sizeOfMat-=1
    print(r2l_element,l2r_element)
    r2l =sum(r2l_element)
    l2r = sum(l2r_element)
    return abs(r2l-l2r)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
