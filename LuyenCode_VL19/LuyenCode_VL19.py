

a, b = [int(x) for x in input().split()]
if(a>b):
    temp=b
    b=a
    a=temp 
   
s=0

while(a+3<b):
    if(a%3==0):
       print(a, end = ' ')
       s=1
    a=a+1

while (a<b):
    if(a%3==0):
        print(a)
        s=1
    a=a+1

if(s==0):
    print("NOT FOUND")

