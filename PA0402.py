# PA0402 - Discard the fractional part

#1.1 A hotel wants to calculate the number of rooms needed for a group of guests. The group of guests intend to save money but sharing rooms, and each room can occupy a maximum of 3 people. Provide code for a python 3 function that returns the minimum number of rooms needed for the guests.

def hotel_rooms(guests):
    return (guests + 2) // 3

#Example
print(hotel_rooms(9))   # 3
print(hotel_rooms(10))  # 4
print(hotel_rooms(1))   # 1
