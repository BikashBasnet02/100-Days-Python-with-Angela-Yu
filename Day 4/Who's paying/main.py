import random

test_seed = int(input('Create a seed number: '))
random.seed(test_seed)

name = input("Give me everybody's names, seperated by comma: ")
names = name.split(", ")

num_items = len(names)

random_choice = random.randint(0, num_items - 1)
pay = names[random_choice]
print(pay + " is going to pay today!")
