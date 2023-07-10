def Nhap():
    n = int(input())
    return n
def InDaoNguoc(n):
    dn = 0
    t = n
    while t != 0:
        dv = t % 10
        dn = dn * 10 + dv
        t //= 10
    return dn
def main():
    n = Nhap()
    print(InDaoNguoc(n))
if __name__ == "__main__":
    main()
