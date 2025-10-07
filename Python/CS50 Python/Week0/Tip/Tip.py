def main():
     Amount=dollar_to_float(input("How much was the meal? "))
     percent=percentage_to_float(input("What percentage would you like to tip? "))
     tip=Amount*percent
     print(f"Leave ${tip:.2f}")





def dollar_to_float(d):
    d=d.replace("$","")
    return float(d)

def percentage_to_float(t):
     t=t.replace("%","")
     return float(t)/100

main()
