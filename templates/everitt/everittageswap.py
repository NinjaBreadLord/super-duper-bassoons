# age1 = 21
# age2 = 16
def ageSwap():
    age1 = input("age 1 :")
    age2 = input("age 2 :")
    if(age2 < age1):
        temp = age1
        age1 = age2
        age2 = temp
    print("age 1 = " + age1,"age 2 =" + age2)
#ageSwap()

#matrix = [ [1,2,3],[4,5,6],[7,8,9] ]
list = [[1,2,3],[4,5,6],[7,8,9]]

def matrix(n):
    for i in n:
         print(*i)

matrix(list)

