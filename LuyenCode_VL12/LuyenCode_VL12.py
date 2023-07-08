def Nhap():
    n = int(input())
    return n
def LietKe(n):
    if n == 0:
        print("INF")
        return
    if n == 1:
        print(n)
        return
    i = abs(n) - 1
    print(abs(n),"",end = "")
    while i >= 2:
        if n % i == 0:
            print(i,"",end = "")
        i-=1
    print(1,end = "")

def main():
    n = Nhap()
    LietKe(n)
if __name__ == "__main__":
    main()
