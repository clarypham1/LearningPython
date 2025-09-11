names = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]
print(names[1])
print(names[1:3])
print(names[-2])
print(len(names))

#### To add a value
names.append("Matti")
print(names)

### To remove a value
names.remove("Pekka")
print(names)

### To add a value in a specific place
names.insert(3, "Samuel")
print(names)

### To add another data set
names2 = ["Allu", "Nimi"]
names.extend(names2)
print(names)

### Find index
Olga = names.index("Olga")
print(Olga)

### Find value in data set
if "Matti" in names:
    print("Matti was found")
else:
    print("Matti was not found")

### sort
names.sort()
print(names)

names.sort(reverse=True)   ##sorted in reverse order
(print(names))

###
names = []

name = input("Add a name to the list:")

while name != "":
    names.append(name)
    name = input("Add other name to the list:")

print(names)