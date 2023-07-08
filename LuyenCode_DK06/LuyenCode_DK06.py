def Nhap():
    a, b = [int(x) for x in input().split()]
    return a,b

def NghiemPTB1(a, b):
    if(a == 0 and b != 0):
        return -1
    if(b == 0 and a == 0):
        return 1
    return 0

def main():
    a, b =Nhap();
    kq = NghiemPTB1(a,b)
    if(kq == 1):
        print("WOW")
    elif(kq == 0):
        x=-b/a
        print('%.2f' % x)
    else:
        print("NO")

if __name__ == "__main__":
    main()