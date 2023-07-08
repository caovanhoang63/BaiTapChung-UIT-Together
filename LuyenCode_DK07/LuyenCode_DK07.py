import math
def Nhap():
    a, b, c= [int(x) for x in input().split()]
    return a, b, c

def NghiemPTB2(a, b, c):
    denta = b*b - 4*a*c
    if(a==0 and b==0 and c==0):
        print("WOW")
    elif(denta < 0):
        print("NO")
    elif(denta == 0):
        x=-b/2*a
        print('%.2f' % x)
    else:
        x1 = (-b - math.sqrt(denta))/2/a
        x2 = (-b + math.sqrt(denta))/2/a
        print('%.2f' % x1,'%.2f' % x2)


def NghiemPTB1(a, b):
    if(a == 0 and b != 0):
        print("NO")
    elif(b == 0 and a == 0):
        print("WOW")
    else:
        x=-b/a
        print('%.2f' % x)

def main():
    a, b, c =Nhap();
    if(a==0):
        NghiemPTB1(b,c)
    else:
        NghiemPTB2(a,b,c)

if __name__ == "__main__":
    main()