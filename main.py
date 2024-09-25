from colored import Fore, Back, Style # type: ignore

from classes.carpark import Carpark # type: ignore
from functions.carpark_functions import add_slot, list_slots, delete_slot, park_car
from functions.file_functions import save_and_exit, load_from_file

print(f"{Fore.yellow}{Back.red}Welcome to Carpark Application!!!{Style.reset}\n")
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

carpark = Carpark("Carparker")

load_from_file(carpark)

while choice != "7":
    choice = create_menu()

    if choice == "1":
        add_slot(carpark)
    elif choice == "2":
        delete_slot(carpark)
    elif choice == "3":
        list_slots(carpark)
    elif choice == "4":
        park_car(carpark)
    elif choice == "5":
        print("Find car")
    elif choice == "6":
        print("Remove car")
    elif choice == "7":
        save_and_exit(carpark)
        print("Exiting")
    else: 
        print("Invalid choice")
print("Thank you for using the Carpark Application!")