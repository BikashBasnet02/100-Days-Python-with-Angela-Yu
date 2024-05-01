import random

player1_grid = [['O' for _ in range(10)] for _ in range(10)]
player2_grid = [['O' for _ in range(10)] for _ in range(10)]

def display_grids(player1_grid, player2_grid):
    print("Player 1's Grid:")
    for row in player1_grid:
        print(" ".join(row))
    print("\nPlayer 2's Grid:")
    for row in player2_grid:
        print(" ".join(row))
    print()

def place_ships(grid):
    ship_lengths = [5, 4, 3, 3, 2]
    for length in ship_lengths:
        while True:
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                if x + length <= 10 and all(grid[y][x+i] == 'O' for i in range(length)):
                    for i in range(length):
                        grid[y][x+i] = 'S'
                    break
            else:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                if y + length <= 10 and all(grid[y+i][x] == 'O' for i in range(length)):
                    for i in range(length):
                        grid[y+i][x] = 'S'
                    break


def take_turn(guess_grid, target_grid):
    while True:
        try:
            x, y = map(int, input("Enter target coordinates (x, y): ").split(','))
            if x < 0 or x > 9 or y < 0 or y > 9:
                print("Invalid coordinates. Please enter values between 0 and 9.")
            elif guess_grid[y][x] != 'O':
                print("You have already guessed these coordinates. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter coordinates in the format 'x, y'.")

    if target_grid[y][x] == 'S':
        print("Hit!")
        guess_grid[y][x] = 'X'
    else:
        print("Miss!")
        guess_grid[y][x] = 'M'

def check_win(grid):
    for row in grid:
        if 'S' in row:
            return False
    return True

def main():
    place_ships(player1_grid)
    place_ships(player2_grid)

    while True:
        display_grids(player1_grid, player2_grid)

        print("Player 1's turn:")
        take_turn(player1_grid, player2_grid)
        if check_win(player2_grid):
            print("Player 1 wins!")
            break

        display_grids(player1_grid, player2_grid)

        print("Player 2's turn:")
        take_turn(player2_grid, player1_grid)
        if check_win(player1_grid):
            print("Player 2 wins!")
            break

if __name__ == "__main__":
    main()
