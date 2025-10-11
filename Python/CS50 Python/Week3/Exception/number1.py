try:
    # Try to convert user input to an integer.
    # If this succeeds, execution continues after the try block and the else block runs.
    x = int(input("What's x? "))
# If the user inputs a non-integer value, handle the exception gracefully
except ValueError:
    # This block runs only if int(...) raised a ValueError.
    # It prevents the program from crashing and gives a user-friendly message.
    print("x is not an integer")
# The else clause runs only when no exception was raised in the try block.
else:
    # Because the conversion succeeded, x is defined here and safe to use.
    print(f"x is {x}")

# Notes:
# - If you put `print(f"x is {x}")` outside the else (below) and the conversion failed,
#   you would get a NameError because x wouldn't be assigned.
# - Exceptions raised inside the else block are NOT caught by the above except.