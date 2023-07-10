n = int(input())
input_str = input()
input_list = input_str.split()


array = [int(item) for item in input_list]

i=0
s=array[0]
a=0
while(i<n):
    if(array[i]>=s):
        s=array[i]
        a=i
    i+=1
print(a)