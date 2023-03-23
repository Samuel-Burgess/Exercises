seats_asked = "NA"
booker_name = "NA"
vehicles = [
    {"number": 1, "type": "Suzuki Van", "seats": 2, "available": True},
    {"number": 2, "type": "Toyota Corolla", "seats": 4, "available": True},
    {"number": 3, "type": "Honda CRV", "seats": 4, "available": True},
    {"number": 4, "type": "Suzuki Swift", "seats": 4, "available": True},
    {"number": 5, "type": "Mitsubishi Airtrek", "seats": 4, "available": True},
    {"number": 6, "type": "Nissan DC Ute", "seats": 4, "available": True},
    {"number": 7, "type": "Toyota Previa", "seats": 7, "available": True},
    {"number": 8, "type": "Toyota Hi Ace", "seats": 12, "available": True},
    {"number": 9, "type": "Toyota Hi Ace", "seats": 12, "available": True},
]

bookings = []


def display_available_vehicles(seats_needed):
    print("Available Vehicles:")
    for vehicle in vehicles:
        if vehicle["available"] and vehicle["seats"] >= seats_needed:
            print(f"{vehicle['number']} - {vehicle['type']} - {vehicle['seats']} seats")
        elif vehicle["available"]:
            print(f"{vehicle['number']} - {vehicle['type']} - Not enough seats")


def book_vehicle(vehicle_number, booker):
    for vehicle in vehicles:
        if vehicle["number"] == vehicle_number:
            booking = {"vehicle": vehicle, "name": vehicle["type"], "Booker": booker}
            bookings.append(booking)
            name = vehicle["type"]
            vehicle["available"] = False
            print(f"You have booked vehicle number {vehicle_number}, a {name}")
            vehicles.remove(vehicle)


while seats_asked != "X":
    booker_name = input("What is your name?: ")
    if booker_name == "X":
        break
    seats_asked = int(input("How many seats do you need?"))
    display_available_vehicles(seats_asked)
    number_needed = int(input("What vehicle number do you want to book?: "))
    book_vehicle(number_needed, booker_name)
for i in bookings:
    print(i)
