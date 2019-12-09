#change for max N numbers, where N is a number typed by the user
list1 = []
num = int(input("Enter number of numbers to compare: "))

for i in range(1, num + 1):
    ele = int(input("Enter number: "))
    list1.append(ele)

print("Largest number is:", max(list1))