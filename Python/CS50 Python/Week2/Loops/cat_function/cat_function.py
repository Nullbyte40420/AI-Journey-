def main():
    n = getnumber()
    meow(n)

def getnumber():
    while True:
        n = int(input("What is n? "))
        if n > 0:
          return n
        
def meow(n):
    for _ in range(n):
        print("Meow")

if __name__ == "__main__":
    main()