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
femalevalue = int(input("Enter the biological gender and hemoglobin value: "))
