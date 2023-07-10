def Runner_up(a, n):
    max = 0
    run = -1
    for i in range(0,n):
        if a[i] >= a[max]:
            max = i
    for i in range(0,n):
        if a[i] != a[max]:
            run = i
    for i in range(0,n):
        if a[i] != a[max] and a[i] >= a[run]:
            run = i
    return run

def main(): 
    n = int(input())
    if n <= 1:
        print("NOT FOUND")
        return
    lst = input().split()
    for i in range(len(lst)):
        lst[i]=int(lst[i])
    kq = Runner_up(lst,n)
    if kq == -1:
        print("NOT FOUND")
    else:
        print(lst[kq])
if __name__ == "__main__":
    main()