import math
def Nhap():
	n = int(input())
	return n

def KiemTra(n):
	if(n <= 0):
		return False
	i = 1
	while(i*i <= n):
		if(i*i == n):
			return True
		i = i + 1
	return False

def main():
	n = Nhap()
	if(KiemTra(n)==True):
		print("YES")
	else:
		print("NO")

if __name__ == "__main__":
    main()