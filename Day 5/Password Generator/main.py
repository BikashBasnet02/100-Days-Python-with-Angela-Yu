import random
import string

print("Welcome to the Password Generator!")

num_letters = int(input('How many letters would you like in your password? '))
num_symbols = int(input('How many symbols would you like? '))
num_numbers = int(input('How many numbers would you like? '))


letters = string.ascii_letters
symbols = '!@#$%^&*()_+[]{}|;:,.<>?'
numbers = string.digits

password_list = []

for _ in range(num_letters):
    password_list.append(random.choice(letters))

for _ in range(num_symbols):
    password_list.append(random.choice(symbols))

for _ in range(num_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ''.join(password_list)

print("Here is your password:", password)
