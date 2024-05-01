# Function to display the main menu
def display_menu():
    print("\n==== TO-DO LIST ====")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Quit")

# Function to add a task to the list
def add_task(task, tasks):
    tasks.append(task)
    print("Task added successfully.")

# Function to view all tasks
def view_tasks(tasks):
    if tasks:
        print("\n==== TASKS ====")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("No tasks found.")

# Main function to run the program
def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter task description: ")
            add_task(task, tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
