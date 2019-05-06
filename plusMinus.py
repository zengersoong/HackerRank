#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive = 0
    negative = 0 
    zero = 0
    total = len(arr)
    for i in range(len(arr)):
        if arr[i] > 0:
            positive += 1
        elif arr[i] < 0:
            negative += 1
        else:
            zero+=1

    p_ratio = positive/total
    n_ratio = negative/total
    z_ratio = zero/total
    # print(p_ratio)
    print(f'{p_ratio:.4f}\n{n_ratio:.4f}\n{z_ratio:.4f}' )       


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
