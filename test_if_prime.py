# generate 100 numbers, print only the prime ones
import random

mylist = []

for i in range(0,100):
    x = random.randint(1,100)
    mylist.append(x)

print("100 random numbers: ",mylist)

for x in range(2,101):
    if all(x%i!=0 for i in range(2,x)):
       print ("Prime numbers: ", x)