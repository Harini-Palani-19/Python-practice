cart = []
while True:
    print("\n1.Add Item")
    print("2.Remove Item")
    print("3.Show Cart")
    print("4.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        item = input("Item name: ")
        cart.append(item)
    elif ch == 2:
        item = input("Item to remove: ")
        if item in cart:
            cart.remove(item)
        else:
            print("Not in cart")
    elif ch == 3:
        print("Cart:", cart)
    elif ch == 4:
        break
