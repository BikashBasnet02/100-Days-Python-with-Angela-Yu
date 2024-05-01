print('Welcome to the rollercoaster! ')
height = int(input('What is your height in cm? '))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input('What is your age? '))
    if age <= 10:
        bill = 5
        print('Please pay $5.')

    elif age <= 18:
        print('Please pay $7.')
        bill = 7
    
    elif age >= 45 and age <= 55: 
        print('Free for you, Have a free ride...')

    else:
        bill = 18
        print('Please pay $18.')

    photo =  input('Do you want a photo taken?(y/n) ').lower()
    if photo == 'y':
        bill += 3
        print(f'Your final bill is ${bill}.')
else:
    print("Sorry, you can't ride the rollercoaster.")
