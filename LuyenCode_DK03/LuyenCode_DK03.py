import math
a,b = [int(x) for x in input().split()]
x = a - b
if x<0:
    print(-x)
else:
    print(x)
