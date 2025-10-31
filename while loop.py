#While loop: works on 1 condition True/False
#For loop

rounds = int(input("How many greetings: "))
finished_round = 0
while finished_round < rounds:
    print("Hello")
    finished_round = finished_round + 1

command = input("Enter command: ")
while command != "stop":
    print("We are free, what to do, lets " + command)
    command = input("Enter command: ")
print("Excecution stopped explicity.")