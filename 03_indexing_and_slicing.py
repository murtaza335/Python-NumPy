import numpy as np

arr = np.array([10, 20, 30, 40, 50])
# indexing the matrix
print(arr[0])      # 10
print(arr[-1])     # 50
print(arr[1:4])    # [20 30 40]

# slicing the matrix
mat = np.array([[1, 2, 3],
                [4, 5, 6]])
print(mat[0, 1])   # Row 0, Col 1 → 2
print(mat[:, 1])   # All rows, Col 1 → [2 5]
print(mat[1, :])   # Row 1, all cols → [4 5 6]
