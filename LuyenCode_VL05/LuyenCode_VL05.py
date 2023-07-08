n=int(input())
s=0
dau=1
if n%2==0:
    for i in range(1,3*n+2):
        s+= dau * i
        dau=-dau
else:
    
    for i in range(1,3*n+2):
        s+= dau * i
        dau=-dau
print(s)