###
colours = ["blue", "res", "orange", "green"]
favcolour = input("What is your favourite colour? ")
if favcolour in colours:
    print("Your favorite colour is found")
else:
    print("Your favourite colour is not found")


####
list = ["eggs", "oil", "milk", "cheese"]
print("glist: ", list)
item = input("What item did you get?")

while item != "":
    list.remove(item)
    item = input("What other item did you get?")
    if item != "eggs" and item !="oil" and item !="milk" and item != "cheese":
        print("Your item is not in the list")
        break
print(list)

###
list = ["eggs", "oil", "milk", "cheese"]
print("glist: ", list)

while list:
    item = input("What item did you get?")
    if item in list:
        list.remove(item)
        print(f"{item} was removed from the list")
        print(list)
    else:
        print("Item is not in the list")
print("Shopping completed")
