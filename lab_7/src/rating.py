from dataclasses import dataclass


@dataclass
class Rating:

    userId: int
    movieId: int
    rating: float
    timestamp: int

    def __str__(self):
        return f'{self.userId}, {self.movieId}, {self.rating}, {self.timestamp}'