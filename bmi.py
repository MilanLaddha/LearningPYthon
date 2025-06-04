h=float(input("Enter your height (in meters):"))
w=float(input("Enter your weight (in kg):"))
b=w/(h**2)
print(b)
if (b<=18.4):
    print("you are under weight")
elif (18.5<=b<=24.9):
    print("you have normal weight")
else :
    print("you are over weight")