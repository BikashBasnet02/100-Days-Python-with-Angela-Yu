print('Welcome to the Love Calculator!')

name1 = input('Please enter your name: ').lower()
name2 = input('Please enter their name: ').lower()

combined_name = name1 + name2

true_count = combined_name.count('t') + combined_name.count('r') + combined_name.count('u') + combined_name.count('e')

love_count = combined_name.count('l') + combined_name.count('o') + combined_name.count('v') + combined_name.count('e')

score = int(str(true_count) + str(love_count))

if score < 10 or score > 90:
    print(f'Your score is {score}%, you go together like coke and mentos.')
elif 40 <= score <= 50:
    print(f'Your score is {score}%, you are alright together.')
else:
    print(f'Your score is {score}%.')
