num1 =int(input("Enter num1: ")) 
num2 = int(input("Enter num2: "))
# printing Input numbers
print(f"num1: {num1} \nnum2: {num2}")
#Arthematic Operations
print(f"Addition operation: {num1 + num2}")
print(f"Substraction operation: {num1 - num2}")
print(f"Multiplication operation: {num1 * num2}")
print(f"Division operation: {num1 / num2}")

#Write a program that accepts a sentence and replace each occurrence of 'python' with 'pythons"
in_str=input("Enter a string: ") 
print(in_str.replace("python", "pythons"))

try:
    score = int(input("Enter Score: "))
except ValueError:
    print("Invalid input. Please enter a valid integer score.")
    exit()  # Exit the program if input cannot be converted to integer

if score >= 90:
    print("Grade is A")
elif score >= 80 and score < 90:
    print("Grade is B")
elif score >= 70 and score < 80:
    print("Grade is C")
else:
    print("Grade is D")



