import numpy as np

def count_sequence_occurrences(arr, seq):
    arr = np.array(arr)
    seq = np.array(seq)
    seq_len = len(seq)
    count = 0
    
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1] - seq_len + 1):
            if np.array_equal(arr[i, j:j+seq_len], seq):
                count += 1
    
    return count

# Example usage:
Arr = [[2, 8, 9, 4],
       [9, 4, 9, 4],
       [4, 5, 9, 7],
       [2, 9, 4, 3]]
seq = [9, 4]

result = count_sequence_occurrences(Arr, seq)
print("Number of occurrences:", result)
