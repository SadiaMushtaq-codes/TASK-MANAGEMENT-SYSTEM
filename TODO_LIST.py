filename = "tasks.txt"
def load_tasks():
    tasks = []
    try:
        with open (filename, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks
def save_tasks(tasks):
    with open(filename, "w")as file:
        for task in tasks:
            file.write(task  +"\n")
def display_menu():
    print("\n ----TO DO LIST----- ")
    print("A. Add a task ")
    print("B.View all tasks ")
    print("C.Remove task by number ")
    print("D.Exit ")
    return input("enter your choice (A/B/C/D): ").strip().lower()
def add_task(tasks):
    task =input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task added :{task}")
    else:
        print("Task cannot be empty.")
    return tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
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
            save_tasks(tasks)
            print("tasks saved. Goodbye!")
            break
        else:
            print("invalid choice, please try again")
if __name__ == "__main__":
    main()
