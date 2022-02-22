# write a python function to swap age with lowest age first\\


def ageswap(age1, age2):
    if (age1 > age2):
        # swapping age by assigning one of them to a temp variable
        temp = age1
        age1 = age2
        age2 = temp
    return(age1, age2)

# this only applies if the file is run as main
if __name__ == "__main__":
    age1 = input("What is the first age?    ")
    age2 = input("What is the second age?   ")
    print("Original: ", age1, age2)
    age1, age2 = ageswap(age1, age2)
    print("Final: ", age1, age2)