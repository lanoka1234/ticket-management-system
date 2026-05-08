# CIS 2368 - Homework 1
import mysql.connector
from datetime import date

# connect to the AWS database
db = mysql.connector.connect(
    host="YOUR_HOST",
    user="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    database="YOUR_DATABASE"
)

# create cursor so we can run SQL queries
cursor = db.cursor()

# main program loop
while True:

    print("\ncn - Check ticket number")
    print("cv - Check ticket validity")
    print("cp - Calculate total price")
    print("rs - Restart")
    print("q - Quit")

    choice = input("Select option: ")

    # check if ticket number exists
    if choice == "cn":
        ticket = input("Enter ticket number: ")
        cursor.execute("SELECT * FROM tickets WHERE ticketno = %s", (ticket,))
        result = cursor.fetchone()

        if result:
            print("Ticket exists")
        else:
            print("Ticket does not exist")

    # check if ticket is still valid
    elif choice == "cv":
        ticket = input("Enter ticket number: ")
        cursor.execute("SELECT validdate FROM tickets WHERE ticketno = %s", (ticket,))
        result = cursor.fetchone()

        if result:
            if result[0] >= date.today():
                print("Ticket is still valid")
            else:
                print("Ticket is expired")
        else:
            print("Ticket does not exist")

    # calculate total price of all tickets
    elif choice == "cp":
        cursor.execute("SELECT SUM(price) FROM tickets")
        result = cursor.fetchone()
        print("Total price:", result[0])

    # restart just goes back to the menu
    elif choice == "rs":
        continue

    # quit program
    elif choice == "q":
        print("Program ended.")
        break

    else:
        print("Invalid option")
