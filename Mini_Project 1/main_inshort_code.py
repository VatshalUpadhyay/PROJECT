# in this code the previous project in less code but readability ni  h
import random
computer=random.choice([-1,0,1])
yourstr=input("Enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"snake",-1:"Water",0:"gun"}
you=youDict[yourstr]
 
print(f"You choose {reverseDict[you]}\nComputer Choice {reverseDict[computer]}")
 
if(computer==you):
    print("Its a draw")

else:
    '''
    if(computer==-1 and you ==1): (computer - you)= -2
        print("You Win")
    elif(computer==-1 and you==0):(computer - you)=-1
        print("You Lose")
    elif(computer==1 and you==-1):(computer - you)=2
        print("You Lose")  
    elif(computer==1 and you==0):(computer - you)=1
        print("You Win")
    elif(computer==0 and you==-1):(computer - you)=1
        print("You Win")
    elif(computer==0 and you==1):(computer - you)=-1
        print("You Lose")
        '''
    if((computer - you)== -1 or (computer-you)== 2 ): # its pattern i analysise from long code in main.py
        print("You lose")
    else:
        print("You Win")

