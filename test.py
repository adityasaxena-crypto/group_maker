import random
names=[]
totnumpep=int(input("Enter the number of people in group: "))
for i in range(totnumpep):
    names.append(input("enter the names:"))
g1=[]
counter=1
a=int(input("Enter group numbers:"))
c=len(names)
peopingrp=int(c/a)
modd=c%peopingrp
if modd==1:
    excep=int(input("in which group do you want extra person:"))
for i in range(a):
    for j in range(peopingrp):
        x=random.randint(0,c-1)
        g1.append(names[x])
        names.pop(x)
        c=c-1
    if counter==excep:
        g1.append(names[0])
        print(g1)
    else:
        print(g1)
    g1=[]
    counter=counter+1