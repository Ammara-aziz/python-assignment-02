#    **Triangle Perimeters**

#    Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle 
# (the sum of all of the side lengths).

# Initialize the perimeter to 0.0 to ensure it's a float
perimeter = 0.0

# Loop to prompt the user for each side length
for i in range(1, 4):
    side_length = float(input(f"What is the length of side {i}? "))
    perimeter += side_length  # or perimeter = perimeter + side_length

# Print the perimeter
print(f"The perimeter of the triangle is {perimeter}")
    



#    Here's a sample run of the program (user input is in bold italics):

   
# What is the length of side 1? 3

#    What is the length of side 2? 4

#    What is the length of side 3? 5.5

#    The perimeter of the triangle is 12.5