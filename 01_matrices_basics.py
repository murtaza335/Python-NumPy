import numpy as np

# matrix A
A = np.array([ [2,2,2], 
              [1,1,1] 
              ])
print(A)
print("multiplied by")
B = np.array([[1,2,3],[2,3,4]])
print(B)

print(A*B)
print("-----")
# following line is the error : because A @ B is the dot product of the 2 matrices 
# and they must be allowed to multiply by their order

# print(A @ B )