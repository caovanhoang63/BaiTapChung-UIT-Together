import math
s = input()
a,b,c = s.split(' ')
a = float(a)

c = float(c)
     
if c == 0:
    print("Math Error")
else:
   if b == '+':
    kq = a + c
   elif b == '-':
        kq =(a - c)
   elif b == '*':
        kq =(a * c)
   elif b == '/':
        kq =(a / c)
   print('{:.2f}'.format(kq))