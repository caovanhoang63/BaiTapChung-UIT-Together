def Nhap():
    n, k = [int(x) for x in input().split()]
    return n, k
def GiaiThua(x):
    i = 1
    t = 1
    while i <= x:
        t *= i
        i += 1
    return t
def main():
    n, k = Nhap()
    kq = GiaiThua(n)/(GiaiThua(k)*GiaiThua(n-k))
    print(int(kq))
if __name__ == "__main__":
    main()

