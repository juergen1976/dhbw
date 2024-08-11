my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]

my_list = [1, 2, 3]
my_list.insert(1, 2.5)
print(my_list)  # Output: [1, 2.5, 2, 3]

my_list = [1, 2, 2, 3]
my_list.remove(2)
print(my_list)  # Output: [1, 2, 3]

my_list = [4, 2, 3, 1]
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4]