#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    stair = []
    for i in reversed(range(n)):
        steps = ''
        r = n - i - 1
        steps += ' ' * r
        steps += '#' * (i+1)
        stair.append(steps)
    stair = stair[::-1]
    return print(*stair,  sep='\n')

if __name__ == '__main__':
    n = int(input())

    staircase(n)
