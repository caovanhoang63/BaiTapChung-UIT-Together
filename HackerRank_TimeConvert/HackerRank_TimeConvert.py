#!/bin/python3

from cgi import print_arguments
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
    min_sec = s[2:8] 
    print(min_sec)
    print(s[8])
    hour = int(s[0:2])
    print(hour)
    if (s[8] == 'P' and hour < 12):
        hour = hour + 12
    if (s[8] == 'A' and hour == 12): 
        hour = 0
    result =''
    if (hour < 10):
        result = '0' +str(hour) + min_sec
    else:
        result = str(hour) + min_sec;
    return  result

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)
    print(result)