# student data 
student_numbers = ["2023-0001", "2023-0002"]
student_names = ["Dela Cruz, Juan", "Santos, Maria"]
balances = [150.00, 200.00]

# menu data
items = ["Burger", "Fries", "Hotdog", "Juice"]
prices = [35.00, 30.00, 25.00, 20.00]

# parallel lists for tracking
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
    print("\n Press 0 to exit")

    choice = input("Choose item number: ")

    # NEW: checks if the input is all digits and if it is, then turns it into an integer
    if choice.isdigit():
        choice_inputed = int(choice)
        # prepares for the calculation of the cost
        item_index = choice_inputed - 1
        cost = prices[item_index]
        # NEW: cancels transaction if the variable choice_inputed == 0
        if not choice_inputed == 0:
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
            print("Transaction cancelled. ")
    else:
        print("Error: Please enter a number. ")
else:
    print("Student not found")
    
