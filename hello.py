
#Types of variables based on data types
# 1. numeric data types:
#int: whole number
#float: decimal
#complex: real + imaginary numbers

#2. string
#3. Booleom Tre/False
#4. tuple ()
#5. dictionary
#6. list
#7. set

programming = float(input("Enter your programming score: "))
print (programming)
physics = float(input("Enter your physics score: "))
print (physics)
mathematics = float(input("Enter your mathematics score: "))
print (mathematics)

percentage1 = int(programming/(physics+programming+mathematics)*100)
print ("The percentage of programming score is:", percentage1, "%")
percentage2 = int(physics/(physics+programming+mathematics)*100)
print ("The percentage of physics score is:", percentage2, "%")
percentage3 = int(mathematics/(physics+programming+mathematics)*100)
print ("The percentage of mathematics score is:", percentage3, "%")

