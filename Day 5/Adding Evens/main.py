sum = 0
number = int(input('Enter the number you wanna add: '))  
for n in range(1, number + 1):   
    if n % 2 == 0:
        sum += n 
print(f'Total sum of even numbers up to 1 to {number} = {sum}')
