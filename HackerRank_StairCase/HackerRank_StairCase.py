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
    s = ''
    for i in range(1,n+1):
        for j in range(1,n - i +1 ):
            s+=" ";
        for j in range (1 ,i + 1):
            s+="#";
        print(s)
        s = ''
    

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
