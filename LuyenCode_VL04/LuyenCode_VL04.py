n = int(input())
Sum = 0
i = 2
while(i <= n):
    Sum = Sum + float(1/i)
    i = i + 1

print('%.4f' % round(Sum,4))