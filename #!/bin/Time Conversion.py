#  Time Conversion

#  HackerRank Problem Solved using Python.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    
    l=s.split(":")
    if(l[2][2:4]=="PM" and int(l[0])>=1 and int(l[0])<12):
        a=str(int(l[0])+12)+":"+l[1]+":"+l[2][0:2]
        return a
    if (l[2][2:4]=="AM" and int(l[0])==12):
        a="00"+":"+l[1]+":"+l[2][0:2]
        return a
    if(l[2][2:4]=="PM" and int(l[0])==12):
        a=l[0]+":"+l[1]+":"+l[2][0:2]
        return a
    if (l[2][2:4]=="AM" and int(l[0])>=1 and int(l[0])<12):
        a=l[0]+":"+l[1]+":"+l[2][0:2]
        return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
