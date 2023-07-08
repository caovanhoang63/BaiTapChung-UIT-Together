def Nhap():
    a, b =[int(x) for x in input().split()]
    return a, b

def Simplify_Fractions(a, b):
    x = abs(a)
    y = abs(b)
    while(x != y):
        if(x > y):
            x = x - y
        else:
            y = y - x
    a = int(a/x)
    b = int(b/x)
    return a, b


def main():
    a, b = Nhap()
    if(b == 0):
        print("INVALID")
        return
    if(a == 0 and b != 0):
        print(0)
        return
    a, b = Simplify_Fractions(a, b)
    if(a*b > 0 and (b == 1 or b == -1)):
        print(a*b)
    elif(a*b < 0 and (b == 1 or b == -1)):
        print(a*b)
    elif(a*b > 0):
        print(abs(a),abs(b))
    else:
        print(a,b)
    return


if __name__ == "__main__":
    main()