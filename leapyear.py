a=float(input("enter a year (in for XXXX):"))
b=a%4
if b==0:
    c=a%100
    if c==0:
        d=a%400
        if d==0:
            print("it is a leap year")
        else:
            print("it is not a leap year")
    else:
        print("it is a leap year")
else:
    print("it is not a leap year")