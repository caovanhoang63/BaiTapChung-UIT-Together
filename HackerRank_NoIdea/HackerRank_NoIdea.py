def Nhap():
    Result=[int(x) for x in input().split()]
    return Result
def NhapSo():
    a,b=[int(x) for x in input().split()]
    return a,b
def Feeling(D,A,B):
    Feel=0
    for i in range(len(D)):
        if (D[i] in A):
            Feel+=1
        elif (D[i] in B):
            Feel-=1
    return Feel
def main():
    n,m=NhapSo()
    D=Nhap()
    A=Nhap()
    B=Nhap()
    print(Feeling(D,A,B))
if __name__=='__main__':
    main()
