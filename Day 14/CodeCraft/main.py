class CodeCraftInterpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, code):
        tokens = code.split()
        if len(tokens) == 3:
            if tokens[1] == "=":
                try:
                    result = eval(tokens[2], self.variables)
                    self.variables[tokens[0]] = result
                    print(f"{tokens[0]} = {result}")
                except:
                    print("Error! Invalid expression.")
            else:
                print("Error! Invalid syntax.")
        else:
            print("Error! Invalid syntax.")

def main():
    interpreter = CodeCraftInterpreter()

    print("Welcome to CodeCraft Interpreter!")
    print("You can assign values to variables and perform basic arithmetic operations.")
    print("Example: a = 5 + 3")

    while True:
        code = input("\nEnter your code (or type 'exit' to quit): ")
        if code.lower() == 'exit':
            print("Exiting CodeCraft Interpreter...")
            break
        else:
            interpreter.interpret(code)

if __name__ == "__main__":
    main()
