#Create a Python Program to Display the Shopping List of a Person

items=[]
cost=[]
total=0.0

while True:
    food=input("Enter the food item Or Press q to exit ")
    if(food=="q"):
        break
    else:
        items.append(food)
        prices=float(input(f"Enter the price of {food} "))
        cost.append(prices)

# for i in prices: Error Given as float object is not iterable
#     print(prices)

print("----- YOUR CART -----")
for i in items:
    print(i,end=" ")

print()
print(f"Your total cost is {sum(cost)} Rs")
