# Unpacking a tuple into variables
numbers = (1, 2, 3)
a, b, c = numbers
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# Using an asterisk to capture remaining items
fruits = ("apple", "banana", "cherry", "date")
first_fruit, *remaining_fruits = fruits
print(first_fruit)  # Output: apple
print(remaining_fruits)  # Output: ['banana', 'cherry', 'date']
