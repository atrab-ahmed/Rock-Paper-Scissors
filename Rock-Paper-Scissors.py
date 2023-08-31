import random
choices=["rock","paper","scissors"]
tries=6
user_score=0
computer_score=0

while tries>0:
    Usre_Choise=input("enter your Choise (rock , paper , scissors)").lower()
    while Usre_Choise not in choices:
        Usre_Choise=input("Wrong choise, please try again \nEnter your Choise (rock , paper , scissors)").lower()
        
    Computer_Choise=random.choice(choices)
    print(f"Your Choise: {Usre_Choise}, Computer Choise: {Computer_Choise}")

    if Usre_Choise == Computer_Choise:
        print("It is a tie!")

    elif Usre_Choise == "scissors":
        if Computer_Choise == "paper":
            user_score+=1
            print("You scored 1 point")
        else:
            computer_score+=1
            print("Computer scored 1 point")

    elif Usre_Choise == "rock":
        if Computer_Choise == "scissors":
            user_score+=1
            print("You scored 1 point")
        else:
            computer_score+=1
            print("Computer scored 1 point")
    
    elif Usre_Choise == "paper":
        if Computer_Choise == "scissors":
            user_score+=1
            print("You scored 1 point")
        else:
            computer_score+=1
            print("Computer scored 1 point")
    
    print(f"Your scored: {user_score} , Computer scored: {computer_score} ")
    tries-=1

print("Game Over")
if user_score > computer_score:
    print("You Win")
elif user_score < computer_score:
    print("Computer Win")
else:
    print("Tie!")

