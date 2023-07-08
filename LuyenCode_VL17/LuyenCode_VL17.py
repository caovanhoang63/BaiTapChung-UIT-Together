n=int(input())
if(n<0):
    n=-n
dem=0
for i in range(1,n+1):
    if(n%i==0):
        dem+=1
    i+=1
print(dem)