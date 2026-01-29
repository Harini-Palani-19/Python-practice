balance = 1000

while True:
    print("\n1.Deposit  2.Withdraw  3.Check Balance  4.Exit")
    choice = int(input("Choice: "))

    if choice == 1:
        amt = int(input("Amount: "))
        balance += amt

    elif choice == 2:
        amt = int(input("Amount: "))
        if amt <= balance:
            balance -= amt
        else:
            print("Insufficient balance")

    elif choice == 3:
        print("Balance:", balance)

    elif choice == 4:
        break
