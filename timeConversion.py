#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    new_hour=''
    if s[:2]=='12' and "AM" in s:
        s = '00'+ s[2:-2]
        return s
        # else: "AM" in s:
    elif "AM" in s:
        return s[:-2]
    elif "PM" in s:
        if s[:2] == '12':
            return s[:-2]
        new_hour = int(s[:2])+12
        s = str(new_hour) + s[2:-2] 
        return s

        

    #
    # Write your code here.
    #

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
