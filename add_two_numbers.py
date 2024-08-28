# **Add two numbers**

#    Write a Python program that takes two integer inputs from the user and calculates their sum. 
# The program should perform the following tasks:


#    1. Prompt the user to enter the first number.
first_num = input("Enter the first number: ")

#    2. Convert the input to an integer
fst_num = int(first_num)

#    3. Prompt the user to enter the second number
sec_num = input("Enter the second number:")

#    4. Convert the input to an integer
sc_num = int(sec_num)

#    5. Calculate the sum of the two numbers
sum = fst_num + sc_num
print(f"The sum of {fst_num} and {sc_num} is {sum}")
