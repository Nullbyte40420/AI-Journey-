def main():
    x,y,z=input("Expression: ").split()
    x=int(x)
    z=int(z)
    ans= operation(x,y,z)
    print(f"{ans:.1f}")



def operation(x,y,z):
    if y=="+":
        return x+z
    elif y=="-":
        return x-z
    elif y=="*":
        return x*z
    elif y=="/":
        if z!=0:
            return x / z
        else:
            print("Error: division by zero")
    else:
        print("Invalid operator")

main()