'''
1 for snake
-1 for water
0 for gun
'''
import random
computer=random.choice([-1,0,1])
yourstr=input("Enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"snake",-1:"Water",0:"gun"}
you=youDict[yourstr]
# Now we have 2 number you and computer 
print(f"You choose {reverseDict[you]}\nComputer Choice {reverseDict[computer]}")
# here the number which convert by you in(line 11)again convert from reversedict 
if(computer==you):
    print("Its a draw")
else:
    if(computer==-1 and you ==1): 
        print("You Win")
    elif(computer==-1 and you==0):
        print("You Lose")
    elif(computer==1 and you==-1):
        print("You Lose")  
    elif(computer==1 and you==0):
        print("You Win")
    elif(computer==0 and you==-1):
        print("You Win")
    elif(computer==0 and you==1):
        print("You Lose")
    else:
        print("Something Wrong")
