#  Staircase

#  HackerRank problem Solved using Python.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    t=n
    for i in range(1,n+1):
        print(" "*(t-1)+"#"*i)
        t-=1

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
