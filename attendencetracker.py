present = []
while True:
    print("\n1.Mark Present")
    print("2.Show Present List")
    print("3.Total Present")
    print("4.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        name = input("Student name: ")
        present.append(name)
    elif ch == 2:
        print("Present Students:", present)
    elif ch == 3:
        print("Total =", len(present))
    elif ch == 4:
        break
