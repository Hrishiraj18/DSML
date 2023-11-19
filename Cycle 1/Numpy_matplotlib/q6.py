import numpy as np
print("Enter the coordinates of first point : ")
point1=[]
point2=[]
for i in range(3):
    coordinate=int(input())
    point1.append(coordinate)

print("Enter the coordinates of second point : ")
for i in range(3):
    coordinate=int(input())
    point2.append(coordinate)
print(point1 ,point2)
point1=np.array(point1)
point2=np.array(point2)
euclidean_distance=np.linalg.norm(point2-point1)
print(f" The Eucliden distance is {euclidean_distance}")