import numpy as np
def matrix(r,c):

    matrix=[]
    for i in range(r):
        one_d=[]
        for j in range(c):
            one_d.append(int(input()))
        matrix.append(one_d)
    return matrix
matrix_1=[]
matrix_2=[]
r=int(input("Enter the number of rows"))
c=int(input("Enter the number of columns"))
print("Enter the first matrix details")
matrix_1=matrix(r,c)
print(matrix_1)
print("Enter the second matrix details")
matrix_2=matrix(r,c)
print(matrix_2)
print("The matrix 2 after transpose")
matrix_2=np.transpose(matrix_2)
print(matrix_2)
print("The product of the matrix is : ")
print(np.dot(matrix_2,matrix_1))