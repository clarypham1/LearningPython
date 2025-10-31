students = {
    "Alice": {"Maths": 90, "English": 80,},
    "Bob" : {"Maths": 82, "Sciences": 83} ,

}
print("Alice's maths score:", students["Alice"]["Maths"])
print("Bob's sciences score:", students["Bob"]["Sciences"])

students["Alice"]["History"] = 50

students["Bob"]["Maths"] = 89

students["Seppo"] = {"Biology": 76, "Chemistry": 82,}

del students["Bob"]["Maths"]


print("Whole student dictionary:")
for s in students:
    print(s, students[s])