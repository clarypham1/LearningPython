#1)
seasons = ("Winter", "Spring", "Summer", "Autumn")

def get_season(month):
    if month == 12 or month == 1 or month == 2:
        return seasons[0]
    elif month == 3 or month == 4 or month == 5:
        return seasons[1]
    elif month == 6 or month == 7 or month == 8:
        return seasons[2]
    elif month == 9 or month == 10 or month == 11:
        return seasons[3]
    else:
        return "Invalid month number!"

month = int(input("Enter the number of a month (1-12): "))
print("Season:", get_season(month))

#2)
def main():
    names = set()
    while True:
        name = input("Enter a name: ")
        if name == "":
            break
        if name in names:
            print("Existing name")
        else:
            print("New name")
            names.add(name)
    print("\nNames entered:")
    for n in names:
        print(n)

main()

#3)
def main():
    airports = {}
    while True:
        print("\nChoose an option:")
        print("1 = Enter a new airport")
        print("2 = Fetch airport information")
        print("3 = Quit")
        choice = input("Your choice: ")

        if choice == "1":
            # Enter new airport
            icao = input("Enter ICAO code: ").upper()
            name = input("Enter airport name: ")
            airports[icao] = name
            print("Airport saved!")

        elif choice == "2":

            icao = input("Enter ICAO code: ").upper()
            if icao in airports:
                print("Airport name:", airports[icao])
            else:
                print("No airport found with that ICAO code.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")
