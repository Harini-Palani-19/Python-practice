tasks = []

while True:
    print("\n1.Add 2.View 3.Exit")
    c = int(input("Choice: "))

    if c == 1:
        tasks.append(input("Task: "))
    elif c == 2:
        for t in tasks:
            print("-", t)
    else:
        break
