import json 

file_name = "to_do.json"

def load_tasks():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except:
        return {"tasks": []}

def save_tasks(tasks):
    try:
        with open(file_name, 'w') as file:
            return json.dump(tasks, file)
    except:
        print("failed to save")

def view_tasks(tasks):
    print()
    tasks = tasks["tasks"]
    if len(tasks) <= 0:
        print("No tasks | [Empty]")
    else:
        print("You To-Do list: ")
        for idx, task in enumerate(tasks):
            status = "[Completed]" if task["complete"] else "[Pending]"
            print(f"{idx + 1}. {task['description']} | {status}")

def create_tasks(tasks):
    description = input("Enter your tasks description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
        print("Task add successfully")
    else:
        print("Description can not be empty")

def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        completed_task = int(input("Enter the task number to mark as completed: ").strip())
        
        print("Completed tasks: ", completed_task)

        if 1 <= completed_task <= len(tasks["tasks"]):
            tasks["tasks"][completed_task - 1]["complete"] = True
            save_tasks(tasks)
            print("Task marked completed")
        else:
            print("Invalid number")
    except:
        print("Tasks not Completed")

def delete_tasks(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter task number to delete: ").strip())

    if 1 <= task_number <= len(tasks["tasks"]):
        # if task_number :
        #     print(f"task {task_number} : [Deleted]")
        #     # save_tasks(tasks)
        # else:
        #     print("You can only delete Completed tasks")
        pass
    else:
        print("Enter a valid number")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do list management system.")
        print("1. View tasks")
        print("2. Create tasks")
        print("3. Mark tasks as complete")
        print("4. Delete task")
        print("5. Exit system")

        option = int(input("Enter your option: "))

        if option == 5:
            print("Goodbye")
            break
        elif option == 1:
            view_tasks(tasks)
        elif option == 2:
            create_tasks(tasks)
        elif option == 3:
            mark_task_completed(tasks)
        elif option == 4:
            delete_tasks(tasks)
        else:
            print("Invalid option")

main()