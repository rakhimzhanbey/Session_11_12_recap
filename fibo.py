# determine the N-th number in the fibonacci series (0,1,1,2,3,5,8,) Fn = Fn-1 + Fn-2

import sys
sys.setrecursionlimit(10000)

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

print("fibo(5)=", fibo(5))



n = int(input('Enter : '))
fibo_nums = [0,1]
i=1
if(n==1 or n==2):
    print(n,'th Prime Number is :',fibo_nums[n-1])
    print('Fibonacci Series :', fibo_nums)
elif(n>2):
    while (True):
        fib = fibo_nums[i-1]+fibo_nums[i]
        fibo_nums.append(fib)
        if(len(fibo_nums)==n):
            break
        else:
            i+=1
    print(n,'th Fibonacci Number is :', fibo_nums[n-1])
    print('Fibonacci Series is :', fibo_nums)
else:
    print('Please Enter A Valid Number')