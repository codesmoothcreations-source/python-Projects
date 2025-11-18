import json 

file_name = "to_do.json"

def load_tasks():
    print("tasks List")
    pass

def save_tasks():
    print("task saved")
    pass

def view_tasks():
    print("view tasks")
    pass

def create_tasks():
    print("task created")
    pass

def mark_task_completed():
    print("task completed")
    pass


def main():

    while True:
        print("\nTo-Do list management system.")
        print("1. View tasks")
        print("2. Create tasks")
        print("3. Mark tasks as complete")
        print("4. Exit system")

        option = int(input("Enter your option: "))

        if option == 4:
            break
        elif option == 1:
            load_tasks()

        elif option == 2:
            create_tasks()
            pass
        elif option == 3:
            mark_task_completed()
            pass

main()