while True:
    print("welcome to tip calculator")
    a=float(input("enter the amount: Rs"))
    b=int(input("chose the percentage of tip 10, 12 or 15:"))
    c=int(input("no. of people to divide the bill between:"))
    if b==10:
        d=a*0.10
        print("total bill is "+ str(d+a))
        e=(d+a)/c
        print("each persons total is :",round(e,2))
    elif b==12:
        d=a*0.12
        print("total bill is "+str(d+a))
        e=(d+a)/c
        print("each persons total is :",round(e,2))
    elif b==15:
        d=a*0.15
        print("total bill is "+str(d+a))
        e=(d+a)/c
        print("each persons total is :",round(e,2))
    else:
        print("error in bill creation")
        print("please try again")
    x=input("Do You want to calculate tip again Y or N :")
    if x=='N':
        break
