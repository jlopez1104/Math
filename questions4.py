import math

b = int(input("enter interger b: "))
a = int(input("enter interger a: "))
c = int(input("enter interger c: "))
undersquareroot = b*2-4*a*c
if undersquareroot >0:
    print("please put correct units.")
elif undersquareroot == 0:
    t = (b*-1/2*a)
    print("solution is","x")
else:
    t1 = (b*-1 + math.sqrt(undersquareroot))/2*a
    t2 = (b*-1 - math.sqrt(undersquareroot))/2*a
    print("your solution is t1: ",t1,"and t2: ",t2,)