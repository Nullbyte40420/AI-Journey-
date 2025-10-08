students = [
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
    {"name": "Luna", "house": "Ravenclaw", "patronus": "Hare"},
    {"name": "Cedric", "house": "Hufflepuff", "patronus": "Badger"},

]
for student in students:
    print(f"{student['name']} is in {student['house']} and their patronus is {student['patronus']}")