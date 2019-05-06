#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    lowest_val = min(arr)
    highest_val = max(arr)
    sum_min = sum(arr) - lowest_val
    sum_max = sum(arr)- highest_val
    return(print(sum_max,sum_min))
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
