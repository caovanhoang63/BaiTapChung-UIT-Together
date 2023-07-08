
month, year = [int(x) for x in input().split()]

if(month>=1 and month<=12 and year>0 and year<=100000):
    if (month==1 or month==3 or month ==5 or month==7 or month==8 or month==10 or month==12):
        print(31)
    elif (month==4 or month==6 or month== 9 or month==11):
        print(30)
    elif(month==2):
        if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            print(29)
        else:
            print(28)
else: 
    print("INVALID")

