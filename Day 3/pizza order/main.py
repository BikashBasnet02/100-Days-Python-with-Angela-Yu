print('Welcome yo Pizza Deliveries!')
size = input('What size pizza do you want? small, medium or large(s/m/l): ').lower()
add_pepperoni = input('Do you want pepperoni?(y/n): ').lower()
extra_cheese = input('Do you want extra cheese? (y/n): ').lower()

if size =='s':
    price = 10.50
    if add_pepperoni == 'y':
        price += 0.50
        if extra_cheese == 'y':
            price += 2
            print(f'Your total price is ${price:.2f}')
        else:
            print(f'Your total price is ${price:.2f}')
    elif extra_cheese == 'y':
        price += 2
        print(f'Your total price is ${price:.2f}')

elif size == 'm':
    price = 12.50
    if add_pepperoni == 'y':
        price += 0.50
        if extra_cheese == 'y':
            price += 2
            print(f'Your total price is ${price:.2f}')
        else:
            print(f'Your total price is ${price:.2f}')
    elif extra_cheese == 'y':
        price += 2
        print(f'Your total price is ${price:.2f}')

else:
    price = 14.50
    if add_pepperoni == 'y':
        price += 0.50
        if extra_cheese == 'y':
            price += 2
            print(f'Your total price is ${price:.2f}')
        else:
            print(f'Your total price is ${price:.2f}')
    elif extra_cheese == 'y':
        price += 2
        print(f'Your total price is ${price:.2f}')


print('\nPlease wait for the delivery...')