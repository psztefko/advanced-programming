from property import Property


class House(Property):

    def __init__(self, area: int, rooms: int,
                 price: int, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'House with area: {self.area}' \
               f' square meters with {self.rooms}' \
               f' rooms, placed on {self.address}' \
               f' and costs {self.price}' \
               f' zlotych with plot of size: {self.plot} square meters'
