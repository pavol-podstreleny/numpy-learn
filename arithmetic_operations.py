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


# We can use arithmetic operations between multiple numpy arrays
# They just need to have same dimension or be broadcasted into same dimension
a = np.array([1,2,3,4,5])
b = np.array([10,20,30,40,50])

# Element-wise addition
print(a + b) 


