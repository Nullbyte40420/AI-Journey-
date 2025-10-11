def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x= int(input("What's x? "))

        except ValueError:
            print("x is not an integer")
            # print("x is not an integer")  # Optionally inform the user
        else:
             break
        
    return x

def get_int1():
    while True:
        try:
            x = int(input("What's x? "))
            return x  # Return the valid integer immediately
        except ValueError:
            #print("x is not an integer")
            pass  # Ignore the error and prompt again
        # No else block needed here since we return from the try block

main()