numbers_list = {1,5,2,2,7,7,14,15,13,3,6}
def unique_numbers(numbers_list):
    unique_numbers = set(numbers_list)
    return unique_numbers
print(unique_numbers(numbers_list))

len(unique_numbers(numbers_list))
print(f"the total number of unique numbers is: ", len(unique_numbers(numbers_list)))