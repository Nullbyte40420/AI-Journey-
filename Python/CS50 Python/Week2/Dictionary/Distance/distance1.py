Disctances = {
    "Voyager 1": 163,
    "Voyager 2": 124,
    "Pioneer 10": 122,
    "Pioneer 11": 101,
    "New Horizons": 50
}

def main():
    for distance in Disctances.values(): # Iterate over the values of the dictionary
        print(f"{distance} AU is {convert(distance)} m")
        
def convert(au):
        return au * 149597870700
        

main()