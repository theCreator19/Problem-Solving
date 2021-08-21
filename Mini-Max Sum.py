#  Mini-Max Sum

#  HackerRank Problem Solved using Python.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr=sorted(arr)
    mi,ma=0,0
    for i in range(len(arr)-1):
        mi+=arr[i]
    for i in range(1,len(arr)):
        ma+=arr[i]
    print(mi,ma)       

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
