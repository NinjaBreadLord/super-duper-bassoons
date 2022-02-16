age1 = input("What is the first age?    ")
age2 = input("What is the second age?   ")
# write a python function to swap age with lowest age first\\

print(age1, age2)
def ageswap(age1, age2):
    if (age1 > age2):
        temp = age1
        age1 = age2
        age2 = temp
    return(age1, age2)

age1, age2 = ageswap(age1, age2)
print(age1, age2)