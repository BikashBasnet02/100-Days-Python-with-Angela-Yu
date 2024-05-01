import random

def roll_dice():
    return random.randint(1, 6)

def dice_rolling_simulator():
    print("Welcome to the Dice Rolling Simulator!")
    print("Press enter to roll the dice. Type 'exit' to quit.")
    
    while True:
        user_input = input("Press enter to roll the dice: ").strip().lower()
        
        if user_input == 'exit':
            print("Thanks for playing!")
            break
        
        if user_input == '':
            result = roll_dice()
            print(f"You rolled: {result}")
        else:
            print("Invalid input. Press enter to roll the dice or type 'exit' to quit.")

dice_rolling_simulator()
