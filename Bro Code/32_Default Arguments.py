import time
def count(end,start=0): # if any default argument is passed, they should be written in end
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("Done")
count(10)