#List [] Ordered Changable Duplicate is OK

fruits=["Apples","Banana","Orange","Lichu"]
print(fruits)
print(fruits[0])
print(len(fruits))
print("Apples" in fruits)

for fruit in fruits:
    print(fruit,end=" ")

print()
fruits.append("Pineapple")
print(fruits)

fruits.remove("Lichu")
print(fruits)

fruits.insert(0,"Berry")
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

fruits.clear()
print(fruits)

print(help(fruits))