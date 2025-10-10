def shorten(s):
    result = ""
    for ch in s:
        if ch.lower() not in "aeiou":
            result += ch
    return result
def main():
    s = input("Input: ")
    s = shorten(s)
    print("Output: ", s)

main()