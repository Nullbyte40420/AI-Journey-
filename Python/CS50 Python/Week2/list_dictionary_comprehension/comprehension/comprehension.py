from cs50 import helpers
def main():     
     count = {}
     words = get_words("address.txt")  # Assume this function returns a list of words
     
     for word in words:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

     save_counts(count)  # Assume this function saves the count dictionary

main()
