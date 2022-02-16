list = [ [1,2,3],[4,5,6],[7,8,9] ] 


def matrix(list):
    for i in list:
        print(i[0], i[1], i[2])
            
def othermatrix(list):
    for i in list:
        print(*i)
        

matrix(list)
print("---- OR ----")
othermatrix(list)
