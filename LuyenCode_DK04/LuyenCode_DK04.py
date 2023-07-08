import math
n = float(input())
x = abs(n) - abs(int(n))
if x >= 0.5:
    if n >= 0:
        n = int(n) + 1
    else:
        n = int(n) - 1
else:
    n = int(n)
print(n)