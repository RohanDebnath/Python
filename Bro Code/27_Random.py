import random

print(random.randint(1,100))
print(random.random())

options=["Rock","Paper","Scissors"]
print(random.choice(options))

cards=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
random.shuffle(cards)
print(cards)