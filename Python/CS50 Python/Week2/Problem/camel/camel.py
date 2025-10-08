def main():
    x=input("camelCase: ")
    x=snake_case(x)
    print(f"snake_case: {x}")

def snake_case(x):
    for i in range(len(x)):
        if x[i].isupper():
            x=x[:i]+'_'+x[i].lower()+x[i+1:]

    return x

if __name__ == "__main__":
    main()
