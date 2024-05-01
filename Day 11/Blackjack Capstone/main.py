import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

user_cards = []
computer_cards = []

# Deal initial cards
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

# Game Loop
game_over = False

while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
    else:
        # Ask the user if they want to draw another card
        draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if draw_card == 'y':
            user_cards.append(deal_card())
        else:
            game_over = True

# Show final hands
print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

# Determine the winner
if user_score > 21:
    print("You went over. You lose.")
elif computer_score > 21:
    print("Computer went over. You win!")
elif user_score == computer_score:
    print("It's a draw.")
elif user_score > computer_score:
    print("You win!")
else:
    print("You lose.")
