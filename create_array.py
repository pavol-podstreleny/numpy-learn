import numpy as np

# Numpy array is special type of array that contains items with same data type

# We can create numpy array from traditional python array using np.array()
numbers = np.array([1,2,3,4,5,6])

# We can also create numpy array from csv file using np.genfromtxt()
csv_numbers = np.genfromtxt("numbers.csv",delimiter=",")

print(csv_numbers)
