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
    grouped_tasks = {}
    try:
        with open (filename, "r") as file:
            for line in file:
                task,status,category = line.strip().split("|")
                grouped_tasks.setdefault(category, []).append({"task": task, "status": status})
                # tasks.append({"task" : task, "status": status})
    except FileNotFoundError:
        print("No existing task file found. Starting with an empty task list.")
    return grouped_tasks
def save_all(grouped_tasks):
    with open(filename, "w") as file:
        for category, task_list in grouped_tasks.items():
            for t in task_list:
                file.write(f"{t['task']}|{t['status']}|{category}\n")

def add_task(grouped_tasks):
    task =input("Enter new task: ").strip()
    category = input("Enter category for the task: ").strip()
    if task:
        grouped_tasks.setdefault(category,[]).append({"task" : task , "status" : "pending"})
        print(f"Task added :{task} in category '{category}'")
    else:
        print("Task cannot be empty.")
    # Save tasks after adding a new one
    save_all(grouped_tasks)
    return grouped_tasks
def view_tasks(grouped_tasks):
    if not grouped_tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        count = 1
        for category, task_list in grouped_tasks.items():
            print(f"\nCategory: {category}")
            for task in task_list:
                print(f"{count}. {task['task']} - {task['status']}")
                count += 1
def update_status(grouped_tasks):
    view_tasks(grouped_tasks)
    task_map = {}
    count = 1
    for category,task_list in grouped_tasks.items():
        for idx,task in enumerate(task_list):
            print(f"{count}. [{category}] {task['task']} _ {task['status']}")
            task_map[count] = (category, idx)
            count += 1
    if task_map:
        try:
            num = int(input("Enter the number of the task you want to mark as completed: ").strip())
            if num in task_map:
                category,idx = task_map[num]
                grouped_tasks[category][idx]['status'] = "completed"
                print(f"Task '{grouped_tasks[category][idx]['task']}' marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    save_all(grouped_tasks)
    return grouped_tasks
def remove_task(grouped_tasks):
    task_map= {}
    count = 1
    for category,task_list in grouped_tasks.items():
        print(f"\n Category :{category}")
        for idx,task in enumerate(task_list):
            print(f"{count}. {task['task']} - {task['status']}")
            task_map[count] = (category, idx)
            count += 1
    if task_map:
        try:
            num = int(input("Enter the number of the task you want to remove: ").strip())
            if  num in task_map:
                category,idx = task_map[num]
                removed_task = grouped_tasks[category].pop(idx)
                print(f"Task '{removed_task['task']}' has been removed successfully.")
                if not grouped_tasks[category]:
                    del grouped_tasks[category]
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks to remove.")
    save_all(grouped_tasks)
    return grouped_tasks

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
