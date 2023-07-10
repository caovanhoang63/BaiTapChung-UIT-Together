x, n = [float(z) for z in input().split()]

Sum = 0
i = 1
giaithua = 1
while(i <= n):
    giaithua = giaithua * i
    Sum = Sum + x**i/giaithua
    i = i + 1

print('%.2f' % round(Sum,2))
