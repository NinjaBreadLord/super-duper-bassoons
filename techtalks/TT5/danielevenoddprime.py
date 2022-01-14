import random

def prime(num): 
    prime = True
    for i in range(2, num//2):
        if (num % i) == 0: 
            prime = False
            break
    if prime == True:
        print(i, "is a prime number.")
    else:
        print(i, "is not a prime number.")

def evenodd(num):
    even = False
    if (num % 2) == 0:
        even = True
    if even == True:
        print("It is also an even number.")
    else:
        print("It is also an odd number.")

num = random.randint(1, 100)
prime(num)
evenodd(num)