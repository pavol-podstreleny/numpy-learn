import numpy as np

# We can select the values from numpy array based on index
numbers = np.array([5,2,7,0,11])

print(numbers[0])

# We can also use negative index => same as python
# Select the last element
print(numbers[-1])

# We can use range => same as python
# Numpy array with elements [5,2]
print(numbers[1:3])
