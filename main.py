from random import randint
from time import localtime, mktime



print("Please specify time limit as an integer: ")
timeLimit=int(input())

q_count=0
points=0

a=int(input("Press 1 for addition and subtraction, 2 for multiplication and division: "))

if(a==1):
    input("Press enter to begin: ")

    while True:


        q_count+=1
        first=randint(10,110)
        second=randint(0,first)
        third=first-second
        correct=int()
        tip=randint(1,2)
        if(tip==1):
            #adition
            print(str(third)+" + "+str(second)+" = ",end="")
            correct=first
        elif(tip==2):
            print(str(first)+" - "+ str(second)+" =" ,end="")
            correct=third

        start=mktime(localtime())
        answer=input()
        end=mktime(localtime())

        if(answer.upper()=="X"):
            q_count-=1
            break

        if((end-start)>timeLimit):
            print("You took so long to answer gonna pass this one")
            continue

        try:

            answer=int(answer)
            if(answer==correct):
                print("Right")
                points+=5
            else:
                print("Wrong")
                points-=2
        except ValueError:
            print("Invalid answer :")
            continue

else:
    input("Press enter to begin: ")

    while(True):

        q_count += 1
        first = int()
        second = int()

        correct=int()

        tip=randint(3,4)
        if(tip==3):
            first=randint(5,30)
            second=randint(0,first)
            correct=first*second
            print(str(first)+ " * "+ str(second)+" = ",end="")
        elif(tip==4):
            first=randint(10,200)
            second=randint(1,10)
            correct=first//second
            print(str(first) + " / "+ str(second)+ " = ",end="")


        start = mktime(localtime())
        answer = input()
        end = mktime(localtime())

        if (answer.upper() == "X"):
            q_count -= 1
            break

        if ((end - start) > timeLimit):
            print("You took so long to answer gonna pass this one")
            continue

        try:

            answer = int(answer)
            if (answer == correct):
                print("Right")
                points += 5
            else:
                print("Wrong")
                points -= 2
        except ValueError:
            print("Invalid answer :")
            continue


print(str(points))

if((points/5)==q_count):
    print("Super you got all of them right")






