def Nhap():
    return list(map(int, input().split()))

def NhapSo():
    return map(int, input().split())

def Feeling(D,A,B):
    feeling_count = {num: 1 for num in A}
    feeling_count.update({num: -1 for num in B})

    feel = 0
    for num in D:
        if num in feeling_count:
            feel += feeling_count[num]
    
    return feel

def main():
    n, m = NhapSo()
    D = Nhap()
    A = set(Nhap())
    B = set(Nhap())
    print(Feeling(D, A, B))

if __name__ == '__main__':
    main()
