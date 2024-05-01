# Define celebrities
celebrities = {
    "Cristiano Ronaldo": "Portugal",
    "Messi": "Argentina",
    "Meryl Streep": "USA",
    "Leonardo DiCaprio": "USA",
    "Beyoncé": "USA",
    "Taylor Swift": "USA",
    "Marie Curie": "Poland",
    "Albert Einstein": "Germany",
    "Michael Phelps": "USA",
    "Usain Bolt": "Jamaica"
}

# Questions

questions = [
    ("Who has more followers on Instagram:\nA. Cristiano Ronaldo\nB. Messi\nYour Answer: ", "a"),
    ("Who has won more Ballon d'Or awards:\nA. Cristiano Ronaldo\nB. Messi\nYour Answer: ", "a"),
    ("Who has scored more international goals:\nA. Cristiano Ronaldo\nB. Messi\nYour Answer: ", "a"),
    ("Who has won more UEFA Champions League titles:\nA. Cristiano Ronaldo\nB. Messi\nYour Answer: ", "a"),
    ("Who has more Academy Awards (Oscars):\nA. Meryl Streep\nB. Leonardo DiCaprio\nYour Answer: ", "b"),
    ("Who has more Grammy Awards:\nA. Beyoncé\nB. Taylor Swift\nYour Answer: ", "a"),
    ("Who has more Nobel Prizes:\nA. Marie Curie\nB. Albert Einstein\nYour Answer: ", "a"),
    ("Who has more Olympic gold medals:\nA. Michael Phelps\nB. Usain Bolt\nYour Answer: ", "a"),
    ("Who has more Twitter followers:\nA. Cristiano Ronaldo\nB. Messi\nYour Answer: ", "a"),
    ("Who has more Facebook followers:\nA. Messi\nB. Cristiano Ronaldo\nYour Answer: ", "b"),
    ("Who has more YouTube subscribers:\nA. PewDiePie\nB. T-Series\nYour Answer: ", "a"),
    ("Who has more Grand Slam titles:\nA. Serena Williams\nB. Roger Federer\nYour Answer: ", "a"),
    ("Who has more career home runs:\nA. Barry Bonds\nB. Babe Ruth\nYour Answer: ", "a"),
    ("Who has more career assists:\nA. LeBron James\nB. Magic Johnson\nYour Answer: ", "a"),
    ("Who has more Olympic gold medals in gymnastics:\nA. Simone Biles\nB. Larisa Latynina\nYour Answer: ", "a"),
    ("Who has more Formula 1 World Championships:\nA. Lewis Hamilton\nB. Michael Schumacher\nYour Answer: ", "a"),
    ("Who has more career wins in tennis:\nA. Serena Williams\nB. Roger Federer\nYour Answer: ", "a"),
    ("Who has more career goals in NHL:\nA. Wayne Gretzky\nB. Gordie Howe\nYour Answer: ", "a"),
    ("Who has more career three-pointers in NBA:\nA. Ray Allen\nB. Stephen Curry\nYour Answer: ", "a"),
    ("Who has more Tour de France wins:\nA. Lance Armstrong\nB. Eddy Merckx\nYour Answer: ", "a")
]

# Quiz
correct_answers = 0
for i, (question, answer_a, answer_b) in enumerate(questions, 1):
    user_answer = input(question).lower()
    if user_answer == answer_a or user_answer == answer_b:
        print("Correct!\n")
        correct_answers += 1
    else:
        print("Wrong!\n")

    # Ask to continue after every 5 questions
    if i % 5 == 0:
        continue_game = input("Do you want to continue the game? (yes/no): ").lower()
        if continue_game != "yes":
            break

# Display total correct answers
print(f"Total correct answers: {correct_answers}")
