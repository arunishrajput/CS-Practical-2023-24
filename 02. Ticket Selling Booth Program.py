num_people = total_money_collected = tickets_sold = 0

def increment_people():
    global num_people
    num_people += 1

def sell_ticket():
    global num_people, total_money_collected, tickets_sold
    num_people += 1
    tickets_sold += 1
    total_money_collected += 5
    print("Ticket sold!")

def display_num_people():
    global num_people
    print("Number of people visited:", num_people)

def display_tickets_sold():
    global tickets_sold
    print("Number of tickets sold:", tickets_sold)

def display_total_money_collected():
    global total_money_collected
    print("Total money collected:", total_money_collected)

while True:
    print("Enter 1 to increment number of people visited")
    print("Enter 2 to sell a ticket")
    print("Enter 3 to display number of people visited")
    print("Enter 4 to display number of tickets sold")
    print("Enter 5 to display total money collected")
    print("Enter 6 to exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        increment_people()
    elif choice == 2:
        sell_ticket()
    elif choice == 3:
        display_num_people()
    elif choice == 4:
        display_tickets_sold()
    elif choice == 5:
        display_total_money_collected()
    elif choice == 6:
        break
    else:
        print("Invalid choice. Try again.")