# to-do-list
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

tasks = load_tasks()

while True:
    print("\n===== TO-DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if not tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

            try:
                index = int(input("Enter task number to delete: ")) - 1
                tasks.pop(index)
                save_tasks(tasks)
                print("Task deleted successfully!")
            except (ValueError, IndexError):
                print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
