# fruits=["Apples","Orange","Banana","Coconut"]
# vegetables=["Cabbage","carrot","Potatoes"]
# meats=["Chicken","Fish","Turkey"]

# groceries=[fruits,vegetables,meats]
# print(groceries[1][1])

# for collection in groceries:
#     for food in collection:
#         print(food,end=" ")
#     print()


#-----List------
# groceries=[["Apples","Orange","Banana","Coconut"],
#             ["Cabbage","carrot","Potatoes"],
#             ["Chicken","Fish","Turkey"]
#             ]
# for collection in groceries:
#     for food in collection:
#         print(food,end=" ")
#     print()


#-----Tuples-----
# groceries=(["Apples","Orange","Banana","Coconut"],
#             ["Cabbage","carrot","Potatoes"],
#             ["Chicken","Fish","Turkey"]
#             )
# for collection in groceries:
#     for food in collection:
#         print(food,end=" ")
#     print()
 

# -----Set-----
groceries=({"Apples","Orange","Banana","Coconut"},
            {"Cabbage","carrot","Potatoes"},
            {"Chicken","Fish","Turkey"}
            )
for collection in groceries:
    for food in collection:
        print(food,end=" ")
    print()