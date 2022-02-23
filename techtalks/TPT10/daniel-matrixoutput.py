def matrix(list):
    for i in list:
        # prints all elements in each list i 
        print(*i)
    return(list)

# this only applies if the file is run as main
if __name__ == "__main__":
    list = [ [1,2,3],[4,5,6],[7,8,9] ] 
    matrix(list)
