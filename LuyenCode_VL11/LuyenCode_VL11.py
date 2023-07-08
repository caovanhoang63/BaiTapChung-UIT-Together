import math
n = int(input())
dem = 0
i=1
while(i<=math.sqrt(n)):
    if(n%i==0):
        dem+=1
    i+=1
if(dem==2):
    print("YES")
else:
    print("NO")
