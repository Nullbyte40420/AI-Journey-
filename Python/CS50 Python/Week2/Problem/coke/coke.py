def main():
    due = 50
    while True:
        print(f"Amout due: {due}")
        insert = int(input("Insert coin: "))


        due=coin(due,insert)
        
        if due > 0:
                continue
        else:
                if due < 0:
                       due = -due
                print("Change Owed: ", due)
                break
       

               
def  coin(due,insert,):


        if insert in [25,10,5]:
                return due - insert
              
        # elif insert < due:
        else:
              
                return due
         




main()