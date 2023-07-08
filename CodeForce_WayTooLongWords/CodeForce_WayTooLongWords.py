n = int(input())
a = []
for i in range(0,n):
    a.append(input())
for x in a:
    if len(x) <= n:
        print(x)
    else:
        quantity = len(x) - 2
        result = x[0] + str(quantity) +x[len(x)-1]
        print(result)
