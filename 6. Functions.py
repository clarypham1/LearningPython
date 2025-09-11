#1)
import random
def roll_dice():
    return random.randint(1, 6)

result = 0
while result != 6:
    result = roll_dice()
    print(result)

#2)
import random

def roll_dice(sides):
    return random.randint(1, sides)

sides = int(input("How many sides does the dice have? "))

result = 0
while result != sides:
    result = roll_dice(sides)
    print(result)

#3)
def gallons_to_liters(gallons):
    return gallons * 3.78541   # 1 gallon = 3.78541 liters

while True:
    gallons = float(input("Enter volume in gallons (negative number to quit): "))
    if gallons < 0:
        break
    liters = gallons_to_liters(gallons)
    print(f"{gallons} gallons = {liters:.2f} liters")

#4)
def sum_list(numbers):
    return sum(numbers)
my_list = [3, 7, 2, 8, 5]
result = sum_list(my_list)
print("The sum is:", result)

#5)
def remove_odd_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result

original_list = [1, 2, 3, 4, 5, 6, 7, 8]
filtered_list = remove_odd_numbers(original_list)

print("Original list:", original_list)
print("List without odd numbers:", filtered_list)

#6)
