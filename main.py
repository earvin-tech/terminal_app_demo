print("Welcome to the Carpark Application!!!\n")

def create_menu():
    print("Enter 1 to add a parking slot.")
    print("Enter 2 to delete a parking slot.")
    print("Enter 3 to list all the parking slots.")
    print("Enter 4 to park a car.")
    print("Enter 5 to find a parked car.")
    print("Enter 6 to remove a car from the carpark.")
    print("Enter 7 to exit.\n")

    choice = input("Enter your choice: ")

    return choice

choice = ""
while choice != "7":
    choice = create_menu()

    if choice == "1":
        print("Add slot")
    elif choice == "2":
        print("Delete slot")
    elif choice == "3":
        print("List slots")
    elif choice == "4":
        print("Park Car")
    elif choice == "5":
        print("Find car")
    elif choice == "6":
        print("Remove car")
    elif choice == "7":
        print("Exiting")
    else: 
        print("Invalid choice")
print("Thank you for using the Carpark Application!")