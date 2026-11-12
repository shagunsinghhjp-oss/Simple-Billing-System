products = {
    "Rice": 50,
    "Sugar": 40,
    "Oil": 120
}
cart = []
def add_item():
    name = input("Enter product name: ").capitalize()

    if name not in products:
        print("Invalid product. Available: Rice, Sugar, Oil")
        return

    quantity = int(input("Enter quantity: "))

    if quantity < 1:
        print("Quantity must be at least 1.")
        return

    price = products[name]
    amount = price * quantity

    cart.append({
        "name": name,
        "quantity": quantity,
        "price": price,
        "amount": amount
    })

    print(name, "x", quantity, "added | Amount:", amount)

def generate_bill():

    if len(cart) == 0:
        print("Cart is empty!")
        return

    subtotal = 0

    print("\n========== CUSTOMER BILL ==========")

    print("Product\tQuantity\tPrice\tAmount")

    for item in cart:
        print(
            item["name"], "\t",
            item["quantity"], "\t\t",
            item["price"], "\t",
            item["amount"]
        )

        subtotal += item["amount"]

    gst = subtotal * 5 / 100
    grand_total = subtotal + gst

    print("-----------------------------------")
    print("Subtotal:", subtotal)
    print("GST (5%):", format(gst, ".2f"))
    print("Grand Total:", format(grand_total, ".2f"))

    print("===================================")

    save_bill(subtotal, gst, grand_total)

def save_bill(subtotal, gst, grand_total):

    with open("bill.txt", "w") as file:

        file.write("========== CUSTOMER BILL ==========\n")

        for item in cart:
            file.write(
                f"{item['name']} x {item['quantity']} "
                f"= Rs. {item['amount']}\n"
            )

        file.write("-----------------------------------\n")
        file.write(f"Subtotal: Rs. {subtotal}\n")
        file.write(f"GST (5%): Rs. {gst:.2f}\n")
        file.write(f"Grand Total: Rs. {grand_total:.2f}\n")

    print("Bill saved successfully in bill.txt")
while True:

    print("\n===== SIMPLE BILLING SYSTEM =====")
    print("1. Add Item")
    print("2. Generate Bill")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_item()

    elif choice == "2":
        generate_bill()

    elif choice == "3":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice! Try again.")