# Creating a tuple for demonstration
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Slicing from index 2 to 5
slice1 = numbers[2:6]
print(slice1)  # Output: (2, 3, 4, 5)

# Slicing from the beginning to index 4
slice2 = numbers[:5]
print(slice2)  # Output: (0, 1, 2, 3, 4)

# Slicing from index 5 to the end
slice3 = numbers[5:]
print(slice3)  # Output: (5, 6, 7, 8, 9)

# Slicing the entire tuple with a step of 2
slice4 = numbers[::2]
print(slice4)  # Output: (0, 2, 4, 6, 8)

# Reversing the tuple using slicing
reversed_numbers = numbers[::-1]
print(reversed_numbers)  # Output: (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
