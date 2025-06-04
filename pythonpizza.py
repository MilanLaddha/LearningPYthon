while True :
    
    size= input("intupue the size of the pizza S,M or L:")
    n=int(input("number of pizza:"))
    ep= input("do you want extra peporini Y or N:")
    ec= input("do you need extra chess Y or N:")
    bill=0
    if size=='S':
        bill+=150
        if ep=='Y':
            bill+=20
        else:
            bill+=0
    elif size=='M':
        bill+=200
        if ep=='Y':
            bill+=30
        else:
            bill+=0
    elif size=='L':
        bill+=250
        if ep=='Y':
            bill+=30
        else:
            bill+=0
    else:
        print('please input order again')
    if ec=='Y':
        bill+=10
    else:
        bill+=0
    print("total bill : "+str(bill*n)+"Rs")
    x = input("do you want to order again Y or N:")
    if x=='N':
        break