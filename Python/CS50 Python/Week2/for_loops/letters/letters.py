def main():
    names =["alice", "bob", "charlie"]
    for name in names:
        print(write_letter(name.capitalize(), "Princess Peach"))
    # for i in range(len(name)):
        # print(write_letter(name[i].capitalize(), "Princess peach"))
    # print(write_letter("Alice", "princess peach"))
    # print(write_letter("Bob", "the builder"))
    # print(write_letter("Charlie", "the chocolate factory owner"))

def write_letter(name, title):
    return f"""
    +------------------------------+
    dear {name},

    you are invited to my party.
    i hope you can make it!
    sincerely,
    {title}

    +------------------------------+
    """

main()