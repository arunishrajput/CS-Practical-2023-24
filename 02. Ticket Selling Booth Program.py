num_people = money_collected = tickets_sold = 0

def increment_people():
    global num_people
    num_people += 1

def sell_ticket():
    global num_people, money_collected, tickets_sold
    num_people += 1
    tickets_sold += 1
    money_collected += 5
    print("Ticket sold!")

def total():
    print("Number of people visited:", num_people)
    print("Total money collected:", money_collected)

def display_tickets_sold():
    print("Number of tickets sold:", tickets_sold)    

while True:
    print("1. People visited but ticket not sold")
    print("2. People visited and ticket also sold")
    print("3. Display report")
    print("4. Display number of tickets sold")
    print("0. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        increment_people()
    elif choice == 2:
        sell_ticket()
    elif choice == 3:
        total()
    elif choice == 4:
        display_tickets_sold()
    elif choice == 0:
        break
    else:
        print("Invalid choice. Try again.")