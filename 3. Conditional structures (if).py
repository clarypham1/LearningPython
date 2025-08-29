#1)
length = int(input("Enter the length of the zander (cm): "))
limit = 42

if length < limit:
    diff = limit - length
    print(f"Release the fish back into the lake! It is {diff} cm below the size limit.")
else:
    print("Good catch! The zander meets the size limit.")

#2)
cabin = input("Enter the cabin class of a cruise ship (LUX, A, B or C): ")
if cabin == "LUX":
    print("upper-deck cabin with a balcony")
elif cabin== "A":
    print("above the car deck, equipped with a window")
elif cabin== "B":
    print("windowless cabin above the car deck.")
elif cabin=="C":
    print("windowless cabin below the car deck")
else:
    print("Invalid cabin class")

#3)
femalevalue = int(input("If you are female, enter the biological gender and hemoglobin value: "))
if femalevalue < 117:
    print("Your hemoglobin value is low")
elif femalevalue > 155:
    print("Your hemoglobin value is high")
elif 117 <= femalevalue <= 155:
    print("Your hemoglobin value is normal")

malevalue = int(input("If you are male, nter the biological gender and hemoglobin value: "))
if malevalue < 134:
    print("Your hemoglobin value is low")
elif malevalue > 167:
    print("Your hemoglobin value is high")
elif 134 <= malevalue <= 167:
    print("Your hemoglobin value is normal")


#4)
year = int(input("Enter a year: "))
if (year % 4 == 0) and (year % 100 != 0) and (year % 400 == 0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")