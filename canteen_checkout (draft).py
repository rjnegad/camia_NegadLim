# Canteen Self-Checkout Demo (very simple draft)
# Note: This demo has no real security. Anyone who knows a student number can buy items.

# student data in parallel lists
student_numbers = ["2023-0001", "2023-0002"]
student_names = ["Dela Cruz, Juan", "Santos, Maria"]
balances = [150.00, 200.00]

# menu data in parallel lists
items = ["Burger", "Fries", "Hotdog", "Juice"]
prices = [35.00, 30.00, 25.00, 20.00]

# ask for student number
student_no = input("Enter Student Number: ")

if student_no in student_numbers:
    i = student_numbers.index(student_no)
    name = student_names[i]
    balance = balances[i]

    print("Welcome " + name + "! Balance: ₱" + str(balance))

    print("\nMenu")
    for j in range(len(items)):
        print(str(j+1) + ". " + items[j] + " ₱" + str(prices[j]))

    choice = int(input("Choose item number: "))
    cost = prices[choice-1]

    if balance >= cost:
        balances[i] = balance - cost
        print("Bought " + items[choice-1])
        print("New balance: ₱" + str(balances[i]))
    else:
        print("Insufficient funds")
else:
    print("Student not found")
