

class Property():

    def __init__(self, area: int, rooms: int, price: int, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f'Property with area: {self.area}, {self.rooms} rooms, placed on {self.address} and costs {self.price}'