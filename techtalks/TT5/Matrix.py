def matrix(matrix):
        for i in range(len(matrix)):
                for k in range(len(matrix[i])):
                        print(matrix[i][k], end=" ")
                print()

matrix1 = [["rock", "is", "hard"],
           ["run", "make", "tired"],
            ["tree","on","grass"]]

matrix(matrix1)


