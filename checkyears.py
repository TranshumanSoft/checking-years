from datetime import datetime
thisdate = datetime.now()
thisyear = int(thisdate.strftime("%Y"))
print(thisyear)
usyear = int(input("Tell me the year of your birth:"))
stop = thisyear - 120
total = thisyear - usyear
counter = usyear
while True:

    if usyear >= thisyear:
        print("Can you travel to the past? Write again the year of your birth.")
        usyear = int(input("Tell me the year of your birth:"))
    elif usyear < stop:
        print("You cannot write from the grave. Write again the year of your birth.")
        usyear = int(input("Tell me the year of your birth:"))
    else:    
        counter = counter + 1
        print(counter)
        if counter == thisyear:
            print("Here is the list of your years of living over Earth.")
            break
