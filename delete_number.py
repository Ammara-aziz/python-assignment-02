#  **Delete a number**

#    Consider a list named `numbers` with the elements `[1, 2, 3, 4, 5]`. Use list method to delete the number 3?

numbers :list[int] = [1, 2, 3, 4, 5] 
del numbers[2]
print(f'List after deleting the number is {numbers}')





# **Creating a list**

#    You have two lists:

#    - Create a program using list method to add the elements of list2 to list1.

A : list[int] = [1, 2, 3]
B : list[int] = [4, 5, 6]
for i in B:
    A.append(i)
print(f'List after adding the elements of list B is {A}')


# **Pop method**
#    You have a list named items with the elements `[10, 20, 30, 40]`. If you use the `pop` method without any arguments,
# what will the list look like and what value will be removed?

items : list[int] = [10, 20, 30, 40]
print(f"{items.pop()} is removed from the list")


# **Index Method**

#    You have a list called colors with the elements `['red', 'blue', 'green', 'yellow']`. If you use the index method to find 
# the position of 'green', what will the index be?

colors : list[str] = ['red', 'blue', 'green', 'yellow']
print(f"index for {colors[2]} is {colors.index(colors[2])}")
# OR
print(f"index number of green is {colors.index('green')}")


#  **Get last element**
 # Fill out the function `get_last_element(lst)` which takes in a list lst as a parameter and prints the last element in the list. 
# The list is guaranteed to be non-empty, but there are no guarantees on its length.

def get_last_element(lst):
    # Print the last element of the list
    return lst[-1]
print(get_last_element([1, 2, 3, 4, 5]))

# **Get a List**

# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user 
# presses enter without typing anything, print the list.

def get_list_from_user():
    # Initialize an empty list to store user input
    user_list = []
    
    while True:
        value = input("Enter a value: ")
        if value == "":
            break
        user_list.append(value)
    
        
    print(f"Here's the list: {user_list}")

# Call the function to run the program
get_list_from_user()