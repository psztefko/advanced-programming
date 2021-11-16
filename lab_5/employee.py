from library import Library
from datetime import date


class Employee():

    def __init__(self, first_name: str, last_name: str,
                 hire_date: date, birth_date: date, city: str,
                 street: str, zip_code: str, phone: int):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'Employee {self.first_name} {self.last_name}' \
               f' was hired on {self.hire_date}' \
               f' and born on {self.birth_date}' \
               f', live in {self.city} on {self.street}.' \
               f' Zip code {self.zip_code}' \
               f' and phone number: {self.phone}'
