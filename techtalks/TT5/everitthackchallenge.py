import random

j = random.randint(1, 100)


def hack(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")
        for i in range(2, n):
            if (n % i) == 0:
                print("not prime")
                break
            else:
                print("prime")
                break


print(j)
(hack(j))
