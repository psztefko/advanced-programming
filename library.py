

class Library():

    def __init__(self, city: str, street: str,
                 zip_code: str, open_hours: str, phone: int):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Library localised in {self.city}' \
               f' on street {self.street}' \
               f', zip code {self.zip_code}' \
               f', phone {self.phone}' \
               f' and open hours: {self.open_hours}'
