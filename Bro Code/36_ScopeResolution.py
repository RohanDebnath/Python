#variable scope= where the variable is accissiable
#scope resultion = (LEBG) Local-> Enclosed -> Global -> Built in

from math import e

def fun1():
    print(e)
e=5
fun1()
#if e was declared here then e will be not 5