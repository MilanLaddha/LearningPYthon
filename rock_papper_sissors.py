import random

print("""enter:
          0 for rock
          1 for paper
          2 for sissors""")
        

t=0
p=0
while(True):


    user=int(input("Enter user choise:"))
    e=random.randint(0,2)
    print(f"computer choice{e}")
    if (e==user):
        print("Draw")
    elif t<3 and p<3:
        if user>2 or user<0:
            print("input out of bound")
        elif user==0 and e==1:
            print("computer wins the round")
            t+=1
        elif user==0 and e==2:
            print("player wins the round")
            p+=1
        elif user==1 and e==2:
            print("computer wins the round")
            t+=1
        elif user==1 and e==0:
            print("player wins the round")
            p+=1
        elif user==2 and e==1:
            print("computer wins the round")
            t+=1
        elif user==2 and e==1:
            print("player wins the round")
            p+=1
        else:
            print("system error")
            break
    else:
        if t==3:
            print("Computer wins")
            break
        elif p==3:
            print("player wins")
            break
        else:
            print('error')
            break


