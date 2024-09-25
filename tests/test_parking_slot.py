from classes.carpark import Carpark
from functions.carpark_functions import add_slot

def test_add_parking_slot(monkeypatch):
    carpark = Carpark("dummy_name")
    monkeypatch.setattr("builtins.input", lambda _: "PS1")  # type: ignore
    add_slot(carpark)
    slot_found = None
    for slot in carpark.get_slots():
        if slot.id == "PS1":
            slot_found = slot
            break
    assert slot_found