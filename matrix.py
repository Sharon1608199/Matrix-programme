
row = int(input("Enter the number of rows:"))

col = int(input("Enter the number of columns:")) 

matrix = [[0 for x in range(col)] for y in range(row)]

counter = 1                                      

for k in range(col+row-1):
    for j in range(k+1):
        i = k-j

        if (i < row and j < col):

            matrix[i][j] = counter
            counter += 1

for i in range(row):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()
