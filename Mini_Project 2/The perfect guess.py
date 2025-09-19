import random
n= random.randint(1,100) # it generate the random number
a=-1 #ye kabhi hoga ni aur isliye ye baar enter krne ko bolega jab tak guessed na ho jaye
guesses=0
while(a != n):
    guesses +=1
    a=int(input("Guess the number: "))
    if(a>n):
        print("Lower number please")
    else:
        print("Higher number please")
    
print(f"You have guessed the number correctly in {guesses} attempt")