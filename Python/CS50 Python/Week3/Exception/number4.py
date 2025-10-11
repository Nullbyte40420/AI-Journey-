# main is the "caller" — it calls another function (get_int) to get a value.
def main():
    x = get_int("What's x? ")   # main (caller) invokes get_int (callee)
    print(f"x is {x}")

# get_int is the "callee" — it is called by main and is responsible for returning an int.
def get_int(prompt):
    # This function repeatedly prompts until it can safely return an int.
    # Call stack: when main calls get_int, a new frame for get_int is pushed.
    # When get_int returns, that frame is popped and execution continues in main.
    while True:
        try:
            # int(...) may raise ValueError if input is not a valid integer.
            # If conversion succeeds, the value is returned to the caller (main).
            return int(input(prompt))

        except ValueError:
            # The except block handles the ValueError inside the callee.
            # 'pass' means "ignore and loop again" — the caller (main) never sees the ValueError.
            # If we did NOT catch the exception here, it would propagate back to the caller.
            pass

main()