# Note: cleaned up the original code because it was a bit messy
# ==============================
# CANTEEN SELF-CHECKOUT SYSTEM
# ==============================

# ---- STUDENT DATABASE ----
students = {
    "2023-0001": {"name": "Dela Cruz, Juan", "balance": 150.00},
    "2023-0002": {"name": "Santos, Maria", "balance": 200.00}
}

# ---- MENU ----
menu = {
    1: {"name": "Burger", "price": 35.00},
    2: {"name": "Fries", "price": 30.00},
    3: {"name": "Hotdog", "price": 25.00},
    4: {"name": "Juice", "price": 20.00}
}

# ---- GLOBAL SALES TRACKING ----
total_sales = {item: 0 for item in menu}
total_revenue = {item: 0.0 for item in menu}


# ==============================
# MAIN SYSTEM LOOP
# ==============================
while True:
    print("\n" + "=" * 40)
    print("      CANTEEN SELF-CHECKOUT")
    print("=" * 40)

    student_id = input("Enter Student ID (or type 'admin' to close): ").strip()

    if student_id.lower() == "admin":
        break

    if student_id not in students:
        print("Student not found.")
        continue

    student = students[student_id]
    tray = {item: 0 for item in menu}
    tray_total = 0.0

    # ==============================
    # SHOPPING LOOP
    # ==============================
    while True:
        print(f"\nUser: {student['name']} | Balance: ₱{student['balance']:.2f}")
        print(f"Tray Total: ₱{tray_total:.2f}")
        print("-" * 30)

        for num, item in menu.items():
            print(f"{num}. {item['name']} (₱{item['price']}) [In Tray: {tray[num]}]")

        print("\nr - Remove item")
        print("f - Finalize and Pay")
        print("c - Cancel and Logout")

        choice = input("\nSelect option: ").strip().lower()

        # ---- FINALIZE ----
        if choice == "f":
            if tray_total == 0:
                print("Your tray is empty.")
                continue

            if student["balance"] < tray_total:
                print("Insufficient balance.")
                continue

            # Deduct balance
            student["balance"] -= tray_total

            # Update global totals
            for num in menu:
                total_sales[num] += tray[num]
                total_revenue[num] += tray[num] * menu[num]["price"]

            print(f"\nPayment successful! ₱{tray_total:.2f} deducted.")
            break

        # ---- CANCEL ----
        elif choice == "c":
            print("Transaction cancelled.")
            break

        # ---- REMOVE ITEM ----
        elif choice == "r":
            try:
                item_num = int(input("Enter item number to remove: "))
                if item_num not in menu:
                    print("Invalid item number.")
                    continue

                if tray[item_num] == 0:
                    print("No items to remove.")
                    continue

                qty = int(input("Quantity to remove: "))
                if qty <= 0:
                    print("Invalid quantity.")
                    continue

                if qty > tray[item_num]:
                    print("Not that many in tray.")
                    continue

                tray[item_num] -= qty
                tray_total -= qty * menu[item_num]["price"]
                print("Item removed.")

            except ValueError:
                print("Invalid input.")

        # ---- ADD ITEM ----
        else:
            try:
                item_num = int(choice)
                if item_num not in menu:
                    print("Invalid item number.")
                    continue

                qty = int(input("Quantity to add: "))
                if qty <= 0:
                    print("Invalid quantity.")
                    continue

                tray[item_num] += qty
                tray_total += qty * menu[item_num]["price"]
                print("Item added.")

            except ValueError:
                print("Invalid input.")


# ==============================
# FINAL DAILY REPORT
# ==============================
print("\n" + "*" * 35)
print("     FINAL DAILY SALES REPORT")
print("*" * 35)

for num, item in menu.items():
    print(
        f"{item['name']:<10}: "
        f"{total_sales[num]} sold | "
        f"₱{total_revenue[num]:.2f}"
    )
