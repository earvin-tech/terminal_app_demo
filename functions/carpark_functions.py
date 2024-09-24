from classes.parking_slot import ParkingSlot
from classes.car import Car

def add_slot(carpark):
    # Take input the id for the parking slot
    slot_id = input("Enter the id for the parking slot: ")
    # Create an instance of the parking slot
    parking_slot = ParkingSlot(slot_id)
    # Add that slot to the carpark
    carpark.add_slot(parking_slot)
    print("Parking Slot Added\n")

def delete_slot(carpark):
    print("Deleting slot")
    # take input the id of the parking slot
    slot_id = input("Enter the id of the parking slot: ")
    # delete the parking slot
    if carpark.delete_slot(slot_id):
        print("Parking slot deleted\n")
    else:
        print("No parking slot with that id.\n")

def list_slots(carpark):
    all_slots = carpark.get_slots()
    print("\nListing slots...")
    if not all_slots:
        print("No slots found.")
    for slot in all_slots:
        print(slot)
    print("\n")

def park_car(carpark):
    print("Parking a car")
    # Take input the rego of the car
    rego_no = input("Enter the registration number of the car: ")
    # take input the id of the parking slot
    slot_id = input("Enter the id of the parking slot: ")
    # find the parking slot 
    slot_to_park = carpark.find_slot(slot_id)
    if slot_to_park:
        # create instance of the car with rego
        car_to_park = Car(rego_no)
        # add the car to the parking slot
        if (slot_to_park.add_car(car_to_park)):
            print("Car parked successfully\n")
        else:
            print("Car already parked in the slot\n")
    else:
        print("Slot with that id does not exist\n")

    # print("Car parked successfully\n")