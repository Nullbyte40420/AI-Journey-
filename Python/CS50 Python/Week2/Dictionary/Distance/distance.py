Disctances = {
    "Voyager 1": 163,
    "Voyager 2": 124,
    "Pioneer 10": 122,
    "Pioneer 11": 101,
    "New Horizons": 50
}

def main():
    for name in Disctances.keys(): # Iterate over the keys of the dictionary
        print(f"{name} is {Disctances[name]} AU from Earth")

main()
        