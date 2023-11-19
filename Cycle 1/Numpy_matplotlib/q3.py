import numpy as np
n=int(input("Enter the number of items"))
list=[]
for i in range(n):
    number=int(input())
    list.append(number)
k=int(input("Enter the value of k "))
numpy_array=np.array(list)
numpy_array=np.sort(numpy_array)
print(f"{k} smallest items are {numpy_array[:k]}")