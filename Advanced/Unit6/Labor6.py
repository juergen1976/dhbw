# Create a tuple with list of students
student_names = ("John", "Jane", "Bob", "Alice")

# Access the first element of the tuple
print(student_names[0])  # Accessing John

# Convert the tuple to a list
student_list = list(student_names)
print(student_list)

# Convert the list to set
student_set = set(student_list)

# Show memory footprint of the tuple and list and set
import sys
print(f"Tuple size in bytes: {sys.getsizeof(student_names)}")  # 64 bytes # Tuples require less memory than lists because they are immutable and store only the references to the elements.
print(f"List size in bytes: {sys.getsizeof(student_list)}")  # 96 bytes # Lists require more memory than tuples because they store additional information for handling dynamic resizing (e.g., pointers to the next element, previous element, and the list itself).
print(f"Set size in bytes: {sys.getsizeof(student_set)}")  # 728 bytes # Sets require more memory than lists and tuples because they store additional information for maintaining the hash table (e.g., hash values, pointers for handling collisions).

# create iterator object and itrate over it
iterator_object = iter(student_names)
while True:
    try:
        print(next(iterator_object))
    except StopIteration:
        break

# Iterate over the tuple using a for loop
for student in student_names:
    print(student)

# creeate all the elements with numpy
import numpy as np
np_array = np.array(student_names)
# show memory footprint of the numpy array
print(f"NumPy array size in bytes: {sys.getsizeof(np_array)}")  # 96 bytes # NumPy arrays require more memory than tuples because they store additional information for handling multidimensional arrays (e.g., shape, data type, and strides).

# Create 100000 random strings and store them is a list and in numpy array
import random
import string
random_strings = [''.join(random.choices(string.ascii_lowercase, k=10)) for _ in range(100000)]
np_array = np.array(random_strings)
print(f"List size in bytes: {sys.getsizeof(random_strings)}")  # 824464 bytes
print(f"NumPy array size in bytes: {sys.getsizeof(np_array)}")  # 800096 bytes

