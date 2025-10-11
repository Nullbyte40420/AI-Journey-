# RePrompting the user until a valid integer is entered
# Reprompted,break,continue
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
# This loop will continue to prompt the user until a valid integer is entered.
# This code snippet ensures that the user is repeatedly prompted for input until they provide a valid integer.

# After exiting the loop, we can safely use x
print(f"x is {x}")