
# Example 1 - Getting a string from the user
# Input gives what the user types as a string. That is fine here.
name = input("Hi! What's your name? ")
print("Hi " + name + "! How are you today?")



# Example 2 - Getting an integer from the user
# We don't want a string, we want a number, so we surround input with int()
num1 = int(input("Enter a whole number: "))
num2 = int(input("Enter another whole number: "))
answer = num1 + num2
# We want to concatenate strings, so we use str() around the numbers
print(str(num1) + " + " + str(num2) + " = " +  str(answer))

# Example 3 - Getting a float from the user
# We don't want a string, we want a float, so we surround input with float()
num1 = float(input("Enter a number with decimal point: "))
num2 = float(input("Enter another number with a decimal point: "))
answer = num1 + num2
# We want to concatenate strings, so we use str() around the numbers
print(str(num1) + " + " + str(num2) + " = " +  str(answer))