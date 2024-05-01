import random

def simulate_game(state1, state2, game):
    """
    Simulate a game between two states in the specified game.
    Return the winner of the game.
    """
    winner = random.choice([state1, state2])
    print(f"{game} between {state1} and {state2}: {winner} wins!")
    return winner

def main():
    print("Nepal States Games Simulation\n")
    states = []
    num_states = int(input("Enter the number of states participating: "))
    for i in range(num_states):
        state = input(f"Enter name of state {i+1}: ")
        states.append(state)

    games = ["Football", "Cricket", "Volleyball", "Basketball", "Badminton"]

    for game in games:
        print(f"\nSimulating {game}:\n")
        state1 = random.choice(states)
        state2 = random.choice(states)
        while state1 == state2:
            state2 = random.choice(states)
        winner = simulate_game(state1, state2, game)
        print(f"{winner} wins {game}!\n")

if __name__ == "__main__":
    main()
