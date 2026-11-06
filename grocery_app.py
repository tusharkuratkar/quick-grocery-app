items = {
    1: ["Milk (1L)", 60],
    2: ["Bread", 40],
    3: ["Eggs (6)", 54],
    4: ["Rice (1kg)", 80],
    5: ["Chips", 20],
    6: ["Cold Drink", 45],
}

cart = {}
DELIVERY_FREE_ABOVE = 199
DELIVERY_FEE = 25


def show_items():
    print("\nItems available:")
    for k in items:
        print(k, "-", items[k][0], "- Rs.", items[k][1])


def add_item():
    show_items()
    try:
        num = int(input("Item number: "))
        qty = int(input("Quantity: "))
    except ValueError:
        print("Invalid input")
        return
    if num not in items or qty <= 0:
        print("Invalid item or quantity")
        return
    if num in cart:
        cart[num] += qty
    else:
        cart[num] = qty
    print(items[num][0], "added to cart")


def remove_item():
    try:
        num = int(input("Item number to remove: "))
    except ValueError:
        print("Invalid input")
        return
    if num in cart:
        del cart[num]
        print("Removed")
    else:
        print("Item not in cart")


def get_total():
    total = 0
    for k in cart:
        total += items[k][1] * cart[k]
    return total


def show_cart():
    if len(cart) == 0:
        print("Cart is empty")
        return
    print("\n--- YOUR CART ---")
    for k in cart:
        print(items[k][0], "x", cart[k], "= Rs.", items[k][1] * cart[k])
    print("Total: Rs.", get_total())


def checkout():
    if len(cart) == 0:
        print("Cart is empty")
        return
    show_cart()
    total = get_total()
    if total >= DELIVERY_FREE_ABOVE:
        delivery = 0
    else:
        delivery = DELIVERY_FEE
    print("Delivery fee: Rs.", delivery)
    print("Amount to pay: Rs.", total + delivery)
    address = input("Delivery address: ")
    print("Order placed! Delivery in 10 minutes to", address)
    cart.clear()


print("---- QUICK GROCERY ----")
while True:
    print("\n1. Show items")
    print("2. Add to cart")
    print("3. Remove from cart")
    print("4. View cart")
    print("5. Checkout")
    print("6. Exit")
    ch = input("Choose: ")
    if ch == "1":
        show_items()
    elif ch == "2":
        add_item()
    elif ch == "3":
        remove_item()
    elif ch == "4":
        show_cart()
    elif ch == "5":
        checkout()
    elif ch == "6":
        print("Bye")
        break
    else:
        print("Wrong choice")
