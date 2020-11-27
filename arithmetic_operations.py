import numpy as np

#We can add value to the existing numpy array in element-wise fashion

numbers = np.array([1,2,3,4,5])

# There are broadcasting rules applied to make this possible
# 1 is broadcasted into the same shape and repeated over axis with 1 dimension
print(numbers + 1)
print(numbers - 1)
print(numbers / 2)
print(numbers // 2)
print(numbers ** 2)

