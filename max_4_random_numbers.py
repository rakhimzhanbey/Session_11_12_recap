import random
print("This program generates 4 random numbers than prints the biggest one")
a = random.random()*100
b = random.random()*100
c = random.random()*100
d = random.random()*100

print("I have generated these numbers: %.2f %.2f %.2f %.2f" % (a, b, c, d))
if a >= b and a >= c and a >= d:
    print("The biggest number is %.2f" % a)
elif b >= a and b >= c and b >= d:
    print("The biggest number is %.2f" % b)
elif c >= a and c >= b and c >= d:
    print("The biggest number is %.2f" % c)
else:
    print("The biggest number is %.2f" % d)

list1 = [a, b, c, d]

max = max(list1[0], list1[1])
secondmax = min(list1[0], list1[1])

for i in range(2, len(list1)):
    if list1[i] > max:
        secondmax = max
        max = list1[i]
    else:
        if list1[i] > secondmax:
            secondmax = list1[i]

print("Second highest number is : ", str(secondmax))
