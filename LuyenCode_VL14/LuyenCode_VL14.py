
a, b= input().split(' ')

a = ord(a)
b = ord(b)

for code in range(a , b + 1):
    uppercase_char = chr(code).upper()
    print(uppercase_char, end=" ")

