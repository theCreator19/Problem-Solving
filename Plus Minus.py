# Plus Minus

# HackerRank Problem Solved using Python.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    c1,c2,c3=0,0,0
    for i in arr:
        if (i>0):
            c1+=1
        if (i<0):
            c2+=1
        if (i==0):
            c3+=1
            
    c=len(arr)
    print(c1/c)
    print(c2/c)
    print(c3/c)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
