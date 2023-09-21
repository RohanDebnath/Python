set_a=[3,4]
set_b=[1,2]
set_c=set()
i=0
j=0
for i in set_a:
    for j in set_b:
        set_c.add(i,j)
        i+=1
        j+=1
print(set_c)

