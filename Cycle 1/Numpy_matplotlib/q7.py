import numpy as np
row=int(input("Enter the number of rows "))
column=int(input("Enter the number of column "))
print("Enter the contents of array 1")
array1=[]
for i in range(row):
    one_d=[]
    for j in range(column):
        number=int(input())
        one_d.append(number)
    array1.append(one_d)
print(array1)
#next array
print("Enter the contents of array 2")
array2=[]
for i in range(row):
    one_d=[]
    for j in range(column):
        number=int(input())
        one_d.append(number)
    array2.append(one_d)
print(array2)
#coneversion to numpy and operations 
array1=np.array(array1)
array2=np.array(array2)
#operations --
print("Addition of array elements ",array1+array2)
print("Subtraction of array elements ",array1-array2)
print("Multiplication of array elements",array1*array2)
print("Division of array elements ",array1/array2)