import json 

from classes.car import Car
from classes.parking_slot import ParkingSlot

def save_and_exit(carpark):
    json_to_write = []
    for slot in carpark.get_slots():
        if slot.get_car():
            slot_json = {
                "slot_id": slot.get_id(),
                "car": {
                    "registration_number": slot.get_car().get_registration_number()
                }
            }
        else:
            slot_json = {
                "slot_id": slot.get_id()
            }
        json_to_write.append(slot_json)

    with open("data/carpark.json", "w") as json_file:
        json.dump(json_to_write, json_file, indent=4)

def load_from_file(carpark):
    with open("data/carpark.json", "r") as json_file:
        json_to_load = json.load(json_file)

    for slot in json_to_load:
        if slot.get("car"):
            car = Car(slot["car"]["registration_number"])
            slot = ParkingSlot(slot["slot_id"])
            slot.add_car(car)
        else:
            slot = ParkingSlot(slot["slot_id"])
        
        carpark.add_slot(slot)