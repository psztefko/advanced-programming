from dataclasses import dataclass


@dataclass
class Movie:

    movieId: int
    title: str
    genres: str

    def __str__(self):
        return f'{self.movieId}, {self.title}, {self.genres}'