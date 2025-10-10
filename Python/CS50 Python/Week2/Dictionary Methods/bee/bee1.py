words = {"CHAIR": 5,"PAIR": 4,"HAIR": 4,"GRAPHIC": 7 }

def main():
    print("Welcome to Spelling Bee!")
    for word,point in words.items():
        print(f"{word}: {point} points")

main()