def main():
    history = []

    while True:
        action = input("Action: ")

        if action.capitalize() == "Undo":
            undone = history.pop()
            print(f"Undone: '{undone}'")
        elif action == "Restart":
            history.clear()
        else:
            history.append(action)

        print(history)


main()