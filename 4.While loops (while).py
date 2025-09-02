#1)
number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number = number + 1

#2)
while True:
    inches = float(input("Enter a value of inches: "))
    if inches < 0:
        print("Program ended")
        break

    centimeters = inches * 2.54
    print(f"{inches} inches is {centimeters:.2f} centimeters")

#3)
numbers = []
while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break

    num = int(user_input)
    numbers.append(num)

    print("min =", min(numbers))
    print("max =", max(numbers))

#4)
import random
number = random.randint(1, 10)

while True:
    guess = int(input("Give me a number:"))
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("Correct")
        break


#5)

correct_username = "python"
correct_password = "rules"

attempts = 0
max_attempts = 5

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        attempts += 1
        print("Wrong username and/or password")
        print("Try again")
        print("Attempts left: ", max_attempts - attempts)

if attempts == max_attempts:
    print("Access denied")


#6)
import random

points = int(input("Enter points: "))
inside = 0

for i in range(points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x*x + y*y < 1:
        inside = inside + 1

pi = 4 * inside / points

print("Approximate value of pi is:", pi)
