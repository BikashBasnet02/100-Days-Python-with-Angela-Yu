print(''' _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''')

first_number = int(input("What's the first number? "))

print("Addition: + \nSubtraction: - \nMultiplication: * \nDivision: /")
operation = input("Pick an operation: ")

second_number = int(input("What's the second number? "))
if operation == "+":
    print(int(first_number) + int(second_number))
elif operation == "-":
    print(int(first_number) - int(second_number))
elif operation == "*":
    print(int(first_number) * int(second_number))
elif operation == "/":
    print(int(first_number) / int(second_number))
else:
    print("Invalid operation")

