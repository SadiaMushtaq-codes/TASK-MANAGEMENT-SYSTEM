filename = "tasks.txt"
def display_menu():
    print("\n ----TO DO LIST----- ")
    print("A. Add a task ")
    print("B.View all tasks ")
    print("C.Remove task by number ")
    print("D.Mark task as completed ")
    print("E.Exit ")
    return input("enter your choice (A/B/C/D/E): ").strip().lower()
def load_tasks():
    tasks = []
    try:
        with open (filename, "r") as file:
            for line in file:
                task , status = line.strip().split("|")
                tasks.append({"task" : task, "status": status})
    except FileNotFoundError:
        pass
    return tasks
def add_task(tasks):
    task =input("Enter new task: ").strip()
    if task:
        tasks.append({"task" : task , "status" : "pending"})
        print(f"Task added :{task}")
    else:
        print("Task cannot be empty.")
    # Save tasks after adding a new one
    with open(filename, "w")as file:
        for task in tasks:
            file.write(f"{task['task']}|{task['status']}\n")
    return tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['task']} - {task['status']}")
def update_status(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            num = int(input("Enter the number of the task you want to mark as completed: ").strip())
            if 1 <= num <= len(tasks):
                    tasks[num - 1]['status'] = "completed"
                    print(f"Task '{tasks[num - 1]['task']}' marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    return tasks
def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            num = int(input("Enter the number of the task you want to remove: ").strip())
            if 1 <= num <= len(tasks):
                removed_task = tasks.pop(num - 1)
                print(f"Task '{removed_task}' has been removed successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    return tasks

def main():
    tasks= load_tasks()
    while  True:
        choice = display_menu()
        if choice == 'a':
            tasks = add_task(tasks)
        elif choice == 'b':
            view_tasks(tasks)
        elif choice == 'c':
            tasks = remove_task(tasks)
        elif choice == 'd':
            tasks = update_status(tasks)
        elif choice == 'e':
            print("Goodbye!")
            break
        else:
            print("invalid choice, please try again")
if __name__ == "__main__":
    main()
