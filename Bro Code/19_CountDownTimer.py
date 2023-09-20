import time
# time.sleep(3)
# print("Hi")

# my_time=int(input("Enter your time "))
# for i in range(my_time,0,-1): #counting backwards
#     print(i)
#     time.sleep(1)

# print("Times Up")

my_time=int(input("Enter your time "))
for i in range(my_time,0,-1): #counting backwards
    seconds=i%60
    minutes=int(i / 60)%60
    hours=int(i / 3600)
    print(f"{hours:02},{minutes:02},{seconds:02}")
    time.sleep(1)

print("Times Up")