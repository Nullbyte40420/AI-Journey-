def main():
    size = int(input("Enter the size of the box: "))
    print_box(size)


def print_box(size):
    for i in range(size):
        print('*  ' * size)
    
if __name__ == "__main__":
    main()