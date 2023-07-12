import numpy as np

def even_odd(x, y):
    result = []
    if x <= y:
        for i in range(x, y+1):
            result.append(i)
    else:
        for i in range(x, y-1, -1):
            result.append(i)
    return result

x = int(input("Take first int number: "))
y = int(input("Take second int number: "))

result_array = even_odd(x, y)

even_array = [n for n in result_array if n % 2 == 0]
odd_array = [n for n in result_array if n % 2 != 0]

print("Even Array:", even_array)
print("Odd Array:", odd_array)

# Merge even and odd arrays horizontally
merged_array = np.hstack((even_array, odd_array))

print("Merged Array:", merged_array)
