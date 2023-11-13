tasks = []
def menu():
    print("1. Add a task")
    print("2. View tasks")
    print("3. Complete a task")
    print("4. Exit")
def add_task():
    task = input("Enter the task name: ")
    tasks.append({"name": task, "done": False})
def view_tasks():
    for task in tasks:
        if task["done"]:
            print(f"{task['name']} - Done")
        else:
            print(f"{task['name']} - Pending")
def complete_task():
    task_name = input("Enter the task name: ")
    for task in tasks:
        if task["name"] == task_name:
            task["done"] = True
            print("Task marked as done.")
            return
    print("No task found with the given name.")
while True:
    menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_task()
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        complete_task()
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")