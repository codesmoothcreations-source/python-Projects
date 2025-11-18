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
    tasks = tasks["tasks"]
    if len(tasks) <= 0:
        print("No tasks | [Empty]")
    else:
        print("You To-Do list: ")
        for idx, task in enumerate(tasks):
            status = "[Completed]" if ["complete"] else "[Pending]"
            print(f"{idx + 1} {task['description']} | {status}")

def create_tasks(tasks):
    description = input("Enter your tasks description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
    else:
        print("Description can not be empty")

def mark_task_completed():
    print("task completed")
    pass


def main():
    tasks = load_tasks()
    # print(tasks)

    while True:
        print("\nTo-Do list management system.")
        print("1. View tasks")
        print("2. Create tasks")
        print("3. Mark tasks as complete")
        print("4. Exit system")

        option = int(input("Enter your option: "))

        if option == 4:
            print("Goodbye")
            break

        elif option == 1:
            view_tasks(tasks)

        elif option == 2:
            create_tasks(tasks)
            pass
        elif option == 3:
            mark_task_completed()
            pass
        else:
            print("Invalid option")

    # print("Good bey")

main()