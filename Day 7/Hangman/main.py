import random

stages = [
        r"""
           _______
          |       |
          |       O
          |      \|/
          |       |
          |      / \
         _|_
        |   |______
        |          |
        |__________|
        """,
        r"""
           _______
          |       |
          |       O
          |      \|/
          |       |
          |      / 
         _|_
        |   |______
        |          |
        |__________|
        """,
        r"""
           _______
          |       |
          |       O
          |      \|/
          |       |
          |      
         _|_
        |   |______
        |          |
        |__________|
        """,
        r"""
           _______
          |       |
          |       O
          |      \|
          |       |
          |      
         _|_
        |   |______
        |          |
        |__________|
        """,
        r"""
           _______
          |       |
          |       O
          |       |
          |       |
          |      
         _|_
        |   |______
        |          |
        |__________|
        """,
        r"""
           _______
          |       |
          |       O
          |      
          |       
          |      
         _|_
        |   |______
        |          |
        |__________|
        """,
        r"""
           _______
          |       |
          |       
          |      
          |       
          |      
         _|_
        |   |______
        |          |
        |__________|
        """
    ]

word_list = [
    "echo",
    "flame",
    "golf",
    "honey",
    "juice",
    "kiwi",
    "laser",
    "magic",
    "novel",
    "ocean",
    "pearl",
    "quick",
    "robot",
    "sunny",
    "tiger",
    "violet",
    "wagon",
    "xylophone",
    "yacht",
    "zebra"
]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(f'Pstt, solution is {chosen_word}')

display = ["_" for _ in chosen_word]
print(" ".join(display))

while "_" in display and lives > 0:
    guess = input('Guess a letter: ').lower()

    if guess in chosen_word:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
    else:
        lives -= 1
        print("Incorrect guess. You have", lives, "lives left.")

    print(" ".join(display))
    print(stages[lives])

if "_" not in display:
    print("Congratulations! You guessed the word correctly!")
else:
    print("You Lose! The word was:", chosen_word)
