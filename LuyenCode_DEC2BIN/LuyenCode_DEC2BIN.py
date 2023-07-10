def decimal_to_binary(decimal):
    binary = format(decimal, 'b')
    return binary

arr = []
n=int(input())
for i in range(n):
    num = int(input())
    arr.append(num)
for i in range(n):
    binary = decimal_to_binary(arr[i])
    print(binary)
