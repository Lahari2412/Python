# Creating a list of squares using a for loop
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Creating a list of squares using list comprehension
squares = [x ** 2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filtering items using list comprehension
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]