from hotel_classes import *

# Create some services
room_service = Service("Room Service", 20)
laundry_service = Service("Laundry Service", 10)

# Create some guests
guest1 = Guest("John Doe",(2023,4,1))
guest2 = Guest("Bob",(2023, 4, 2))

# Add some services to the guests
guest1.add_service(room_service)
guest2.add_service(room_service)
guest2.add_service(laundry_service)

# Send the bills to the guests
guest1.send_bill()
guest2.send_bill()

# Create some hotel rooms
room1 = Standard(101)
room2 = Suite(201)
room3 = TaylorSuite(301)
room4 = TaylorSuite(302)

# Check some guests into the hotel rooms
room1.guest_check_in(guest1)
room2.guest_check_in(guest2)
room3.guest_check_in(guest2)

# Print the availability status of the hotel rooms
print(f"Room {room1.room_number} is available: {room1.avaliablitystat}")
print(f"Room {room2.room_number} is available: {room2.avaliablitystat}")
print(f"Room {room3.room_number} is available: {room3.avaliablitystat}")
print(f"Room {room4.room_number} is available: {room4.avaliablitystat}")

print(f"Room {room1.room_number} will be available after {room1.avaliable}")
print(f"Room {room2.room_number} will be available after {room2.avaliable}")
print(f"Room {room3.room_number} will be available after {room3.avaliable}")
print(f"Room {room4.room_number} will be available after {room4.avaliable}")

