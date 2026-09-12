import numpy as np

# 1. Create a NumPy Array
arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)

# 2. Array Information
print("Data Type:", arr.dtype)
print("Size:", arr.size)
print("Dimensions:", arr.ndim)

# 3. Create Two Arrays
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

# 4. Basic Numerical Operations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# 5. Mathematical Operations
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
