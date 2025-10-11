# x = int(input("What's x? "))
# # if we input a string, it will raise a ValueError: invalid literal for int() with base 10: 'abc'
# print(f"x is {x}")
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
# If the user inputs a non-integer value, handle the exception gracefully
except ValueError:
    print("x is not an integer")