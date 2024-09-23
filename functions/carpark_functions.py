from classes.parking_slot import ParkingSlot

def add_slot(carpark):
    # Take input the id for the parking slot
    slot_id = input("Enter the id for the parking slot: ")
    # Create an instance of the parking slot
    parking_slot = ParkingSlot(slot_id)
    # Add that slot to the carpark
    carpark.add_slot(parking_slot)
    print("Parking Slot Added\n")

def list_slots(carpark):
    all_slots = carpark.get_slots()
    print("\nListing slots...")
    if not all_slots:
        print("No slots found.")
    for slot in all_slots:
        print(slot)
    print("\n")