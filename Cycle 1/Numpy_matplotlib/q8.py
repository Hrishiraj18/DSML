import numpy as np
matrix=[[1,2,3],[0,1,4],[5,6,0]]
matrix=np.array(matrix)
determinant_of_matrix=np.linalg.det(matrix)
if determinant_of_matrix ==0:
    print("Inverse does not exist")
else:
    inverse=np.linalg.inv(matrix)
    print("The matrix determinant is : ",determinant_of_matrix)
    print("The inverse of matrix is : ",inverse)