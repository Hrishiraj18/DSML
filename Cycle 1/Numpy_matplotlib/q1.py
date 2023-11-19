import numpy as np
n=int(input("Enter the number of entries "))
list=[]
for i in range(n):
    num=int(input())
    list.append(num)
numpy_array=np.array(list)
print("The numpy array is ",numpy_array)
print("The mean of numpy array is ",np.mean(numpy_array))
print("The median of numpy array is ",np.median(numpy_array))
print("The Standard Deviation of numpy array is ",np.std(numpy_array))