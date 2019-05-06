#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    bob_score = 0
    alice_score = 0
    for i in range(3):
        if a[i]>b[i]:
            alice_score+=1
        elif b[i] > a[i]: 
            bob_score+=1
    return [alice_score,bob_score]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
