
a, b = [int(x) for x in input().split()]
s=0 
if(a>b):
    a=b 
    b=a 

while(a<b):
    if(a%2==0):
        s=s+a
    a=a+1
    
if (a==b):
    if(a%2==0):
        s=s+a
print(s)
