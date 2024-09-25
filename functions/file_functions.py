import json 

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

    with open("data/capark.json", "w") as json_file:
        json.dump(json_to_write, json_file, indent=4)