# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and 
# outputs the temperature converted to Celsius.

# Prompt the user for a temperature in Fahrenheit
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

#    **Frenheight/Celcius** -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!

degrees_celsius = 5.0/9.0 * (fahrenheit - 32)  

# Output the temperature in Celsius

print(f"Temperature: {fahrenheit} = {degrees_celsius}C ")

