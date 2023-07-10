
n = int(input())
lst = list(map(int, input().split()))
x=lst[0]

for i in range(0, n):
	if(lst[i]>x):
		x=lst[i]
print(x)