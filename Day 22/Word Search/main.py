import random

def generate_grid(size):
    return [[random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(size)] for _ in range(size)]

def print_grid(grid):
    for row in grid:
        print(' '.join(row))

def search_word(grid, word):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # Define horizontal, vertical, and diagonal directions
    word_length = len(word)
    size = len(grid)

    for i in range(size):
        for j in range(size):
            for dx, dy in directions:
                found = True
                for k in range(word_length):
                    x = i + k * dx
                    y = j + k * dy
                    if x < 0 or x >= size or y < 0 or y >= size or grid[x][y] != word[k]:
                        found = False
                        break
                if found:
                    return True
    return False

def main():
    size = 6 
    words = ['python', 'code', 'programming'] 

    grid = generate_grid(size)
    print_grid(grid)

    found_words = []

    while True:
        guess = input("Enter a word to search (or 'q' to quit): ").lower()
        if guess == 'q':
            break
        if guess in found_words:
            print("You've already found this word!")
            continue
        if search_word(grid, guess):
            print("You found the word '{}'!".format(guess))
            found_words.append(guess)
            if len(found_words) == len(words):
                print("Congratulations! You found all the words!")
                break
        else:
            print("Sorry, the word '{}' is not in the grid.".format(guess))

if __name__ == "__main__":
    main()
