import random
number=random.randint(1,100)
guesses=0

while True:
    choice=int(input("Choose a Number between {1} to {100}"))
    if choice>number:
        print(f"{choice} is too high")
    elif choice<number:
        print(f"{choice} is too low")
    else:
        print("Yes you got it")
        break
    guesses+=1
print(f"You took {guesses} guesses to predict the number")