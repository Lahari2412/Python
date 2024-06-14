# Example: Checking if a number is positive, negative, or zero and if it is even or odd
number = 8

if number > 0:
    print("The number is positive.")
    if number % 2 == 0:
        print("The number is even.")  # Output: The number is positive. The number is even.
    else:
        print("The number is odd.")
elif number < 0:
    print("The number is negative.")
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is zero.")