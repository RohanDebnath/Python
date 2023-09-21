#Set {} Unordred and Immutable , but Add/Remove Ok. No Duplicates


fruits={"Apple","Banana","Coconut"}
print(fruits)
# print(dir(fruits))
print(len(fruits))
print("Coconut" in fruits)

fruits.add("Apple")
print(fruits)
fruits.add("Papita")
print(fruits)

fruits.pop()    #Randomly hobe
print(fruits)

fruits.remove("Apple")
print(fruits)

fruits.clear()
print(fruits)