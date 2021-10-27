from library import Library
from datetime import date

class Book():

    def __init__(self, library: Library, publication_date: date, author_name: str, author_surname: str, number_of_pages: str):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.numer_of_pages = number_of_pages

    def __str__(self):
        return f'Book by {self.author_name} {self.author_surname} publicated on {self.publication_date} can be found in {self.library} has {self.numer_of_pages} pages'