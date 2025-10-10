results =["Mario", "Luigi"]

# for adding an element to the end of the list
results.append("Yoshi")
results.append("Toad")
results.append("Bowser")

results.append(["Peach", "Daisy"]) # This will add a list as a single element
results.remove(["Peach", "Daisy"]) # This will remove the list as a single element
results.extend(["Peach", "Daisy"]) # This will add each element of the list individually
print(results)