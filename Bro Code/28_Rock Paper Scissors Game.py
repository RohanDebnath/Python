import random
options=("Rock","Paper","Scissors")
playing =True
while playing:
    player=None
    while player not in options:
        computer=random.choice(options)
        player=input("Choose Rock, Paper , Scissors ")
    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if(player==computer):
        print("It's a tie")
    elif(player=="Rock"  and computer=="Scissors"):
        print("You win")
    elif(player=="Paper" and computer=="Rock"):
        print("You Win")
    elif(player=="Scissors" and computer=="Paper"):
        print("You win")
    else:
        print("Computer Win")
    Play_again=input("Do you want to play? Y/N ")
    if Play_again=="N":
        playing=False
print("Thank you for playing")

