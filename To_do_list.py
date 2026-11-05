# To-Do List App
# Created by Iram Shehzadi

tasks = []

def show_menu():
    print("\n--- My To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose option (1-4): ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task Added Successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete!")
        else:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Deleted: {removed}")
            else:
                print("Invalid number!")

    elif choice == "4":
        print("Thanks for using To-Do List! Bye Iram!")
        break

    else:
        print("Please choose 1 to 4 only!")