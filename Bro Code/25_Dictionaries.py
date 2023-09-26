
capitals = {"USA": "Washington D.C.",
                    "India": "New Delhi",
                    "China": "Beijing",
                    "Russia": "Moscow"}

print(capitals.get("India"))

if(capitals.get("Japan")):
    print("Capital Existis")
else:
    print("Does not exists")
print(capitals)

capitals.update({"Germany":"Belin"})
print(capitals)

capitals.popitem() #will remove the latest key created
print(capitals)

capitals.pop("USA")
print(capitals)

# capitals.clear()
# print(capitals)

print(capitals.keys())

for key in capitals.keys():
    print(key,end=" ")
print()
for values in capitals.values():
    print(values,end=" ")
print()
for item in capitals.items():
    print(item,end=" ")
print()
print()

for key , value in capitals.items():
    print(f"{key}:{value}")
