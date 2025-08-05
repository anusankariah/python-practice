#simple to-do list
tasks = []
def show_menu():
    print("\nSimple To-Do List")
    print(" 1. Add a task")
    print(" 2. View tasks")
    print(" 3. Remove tasks")
    print(" 4. Exit")

def add_task():
    task = input("Enter a task to add: ")
    tasks.append(task)
    print(f"New {task} added")

def view_tasks():
    if not tasks:
        print("No tasks yet")
    else:
        print("Your tasks")
        for i, task in enumerate(tasks,start=1):
            print(f"{i}. {task}")


def main():
    while True:
        show_menu()
        choice = input(" Choose an option (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "4":
            print("Good Bye")
            break
        else:
            print("Invalid choice. Try again")

#To start the program
if __name__ == "__main__":
    main()





