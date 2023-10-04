import numpy as np
arr = np.array([[1, 0, 3],
                [0, 5, 0],
                [7, 8, 0]])
zero_indices = np.where(arr == 0)
#print(zero_indices)-returns a turple with two list

row_indices, col_indices = zero_indices

for i in row_indices:
    print(f"Element at ({row_indices[i]}, {col_indices[i]}) is equal to zero.")
