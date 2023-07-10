def kiemtraHoanHao(n):
    tong = 0
    for i in range(1, n):
        if (n % i) == 0:
            tong += i
    if tong == n:
        return True
    else:
        return False

n = int(input())
if kiemtraHoanHao(n):
    print("YES")
else:
    print("NO")
