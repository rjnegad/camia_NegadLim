# student data 
student_numbers = ["2023-0001", "2023-0002"]
student_names = ["Dela Cruz, Juan", "Santos, Maria"]
balances = [150.00, 200.00]

# menu data
items = ["Burger", "Fries", "Hotdog", "Juice"]
prices = [35.00, 30.00, 25.00, 20.00]

# NEW: parallel lists for tracking
sales_count = [0, 0, 0, 0]
revenue = [0.0, 0.0, 0.0, 0.0]

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
    item_index = choice - 1
    cost = prices[item_index]

    if balance >= cost:
        balances[i] = balance - cost
        
        # Update tracking lists
        sales_count[item_index] = sales_count[item_index] + 1
        revenue[item_index] = revenue[item_index] + cost
        
        print("Bought " + items[item_index])
        print("New balance: ₱" + str(balances[i]))
        
        # Print summary for this session
        print("\n--- Session Summary ---")
        print("Item: " + items[item_index])
        print("Times bought today: " + str(sales_count[item_index]))
        print("Total item revenue: ₱" + str(revenue[item_index]))
    else:
        print("Insufficient funds")
else:
    print("Student not found")
