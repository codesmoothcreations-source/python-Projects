import json 

#  Config
file_name = "todo_list.json"

def load_tasks():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) :
        return {"tasks": []}

def save_tasks(tasks):
    try:
        with open(file_name, 'w') as item:
            return json.dump(tasks, item)
    except:
        print("failed to save")

def view_tasks(tasks):
    print()
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No tasks to display.")
    else:
        print("Your To-Do List: ")
        for idx, task in enumerate(task_list):
            status = "[Completed]" if task["complete"] else "[Pending]"
            print(f"{idx + 1}. {task['description']} | {status}")

def create_tasks(tasks):
    description = input("Enter the task description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
        print("task added.")
    else:
        print("Description can not be empty")

def mark_tasks_complete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as complete: ").strip())
        if 1 <= task_number <= len(tasks):
            tasks["tasks"][task_number - 1]["complete"] = True
            save_tasks(tasks)
            print("Task marked Complete.")
        else:
            print("Invalid number")
    except:
        print("Enter a valid task number.")

def main():
    tasks = load_tasks()
    # print(tasks) 

    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Tasks")
        print("3. Complete Task")
        print("4. Exit")

        choice = int(input("Enter your choice: ").strip())

        if choice == 1:
            view_tasks(tasks)
        elif choice == 2:
            create_tasks(tasks)
        elif choice == 3:
            mark_tasks_complete(tasks)
        elif choice == 4:
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please try again.")

main()