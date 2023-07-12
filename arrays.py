import numpy as np


def create_3d_array():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    depth = int(input("Enter the depth: "))
    
    arr = np.empty((rows, cols, depth))
    
    for i in range(rows):
        for j in range(cols):
            for k in range(depth):
                element = float(input(f"Enter the value for element ({i}, {j}, {k}): "))
                arr[i, j, k] = element
    
    return arr


array1 = create_3d_array()
array2 = create_3d_array()
array3 = create_3d_array()

print("Array1: ",array1)
print("Array2: ",array2)
print("Array1: ",array3)

result1 = np.concatenate((array1, array2), axis=2)
result2 = np.concatenate((result1, array3), axis=2)

print("Result 1:")
print(result1)
print("Result 2:")
print(result2)
