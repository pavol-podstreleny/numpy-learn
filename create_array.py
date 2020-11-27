import numpy as np

# Numpy array is special type of array that contains items with same data type

# We can create numpy array from traditional python array using np.array()
numbers = np.array([1,2,3,4,5,6])

# We can also create numpy array from csv file using np.genfromtxt()
csv_numbers = np.genfromtxt("numbers.csv",delimiter=",")

print(csv_numbers)

# We can also create multi-dimensional numpy array
matrix = np.array([[92,94,88,91,87],
                   [79,100,86,93,91],
                   [87,85,92,90,92]])
print(matrix)
