class Question:
    def __init__(self, question_id: int, question: str, answer_a: str, answer_b: str, answer_c: str, answer_d: str, correct_answer: str):
        self.question_id = question_id
        self.question = question
        self.answer_a = answer_a
        self.answer_b = answer_b
        self.answer_c = answer_c
        self.answer_d = answer_d
        self.correct_answer = correct_answer
    
    def validate_answer(self, user_answer):
        return user_answer == self.correct_answer
    
    def print_question(self):
        print(f"Question {self.question_id}: {self.question}")
        print("Options:")
        print("A. ", self.answer_a)
        print("B. ", self.answer_b)
        print("C. ", self.answer_c)
        print("D. ", self.answer_d)


questions = [
    Question(1, "What is the capital of India?", "Delhi", "Mumbai", "Chennai", "Kolkata", "A"),
    Question(2, "Which planet is known as the Red Planet?", "Mars", "Venus", "Jupiter", "Saturn", "A"),
    Question(3, "Who wrote 'To Kill a Mockingbird'?", "Harper Lee", "J.K. Rowling", "Stephen King", "George Orwell", "A"),
    Question(4, "What is the chemical symbol for water?", "H2O", "CO2", "O2", "CH4", "A"),
    Question(5, "What is the largest mammal?", "Elephant", "Whale", "Giraffe", "Hippo", "B"),
    Question(6, "What is the capital of France?", "Berlin", "Paris", "London", "Rome", "B")
]


for q in questions:
    print("Question ID : ", q.question_id)
    print("Question : ", q.question)
    print("Options:")
    print("A. ", q.answer_a)
    print("B. ", q.answer_b)
    print("C. ", q.answer_c)
    print("D. ", q.answer_d)
    user_answer = input("Your answer (A/B/C/D): ").upper()
    if q.validate_answer(user_answer):
        print("Correct!")
    else:
        print("Incorrect. The correct answer is", q.correct_answer)

    print()  
