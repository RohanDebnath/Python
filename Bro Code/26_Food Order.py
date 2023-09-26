menu = {"pizza": 3.00,
               "nachos": 4.50,
               "popcorn": 6.00,
               "fries": 2.50,
               "chips": 1.00,
               "pretzel": 3.50,
               "soda": 3.00,
               "lemonade": 4.25}
cart=[]
total=0

print("-----Menu-----")
for food,price in menu.items():
    print(f"{food:10}: {price:.2f}")

while True:
    food=input("Please Select a food Item (q to quit)").lower()
    if food=='q':
        break
    elif(menu.get(food)is not None):
       cart.append(food)

print("-----Your Oder-----")
for food in cart:
    total+=menu.get(food)
    print(food,end=" ")

print()
print(f"Your Total is $ {total}")