words = {"CHAIR": 5,"PAIR": 4,"HAIR": 4,"GRAPHIC": 7 }

def main():
    print("Wellcome to the word score program!")
    print("your letters are: A, C, G, H, I, P, R")
    score = 0 
    while len(words) > 0:
        word = input("Enter a word : ").upper()

        # TODO: check if the word is valid
        if word == "GRAPHIC":
            print("Congratulations! You won")
            words.clear()

        if word in words:
            score += words.pop(word)
            print(f"Your score is {score}")
        print(f"{len(words)} word left")
    print("That's The game")    

main()