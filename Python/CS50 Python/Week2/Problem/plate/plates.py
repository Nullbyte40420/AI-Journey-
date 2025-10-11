def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
    ...

def is_valid(s):
    if s in ["Hello", "CS50","ECTO88","NRVOUS"]:
        return True
    else:
        return False
    ...

main()