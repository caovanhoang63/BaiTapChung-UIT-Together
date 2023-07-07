a, b = [int(x) for x in input().split()]
print(a+b)
print(a-b)
print(a*b)
if b != 0:
    print("{:.2f}".format(a/b))
else:
    print("ERROR")



