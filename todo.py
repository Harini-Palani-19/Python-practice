tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif ch == 2:
        if not tasks:
            print("No tasks yet.")
        else:
            for i, t in enumerate(tasks, 1):
                print(i, t)

    elif ch == 3:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Deleted!")
        else:
            print("Invalid number")

    elif ch == 4:
        print("Goodbye ")
        break

    else:
        print("Invalid choice")
