def uscln(a, b):
    if (b == 0):
        return a;
    return uscln(b, a % b);
def bscnn(a, b):
    return int((a * b) / uscln(a, b));
a, b = [int(x) for x in input().split()]
print(abs(bscnn(a,b)))