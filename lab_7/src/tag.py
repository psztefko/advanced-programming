from dataclasses import dataclass


@dataclass
class Tag:

    userId: int
    movieId: int
    tag: str
    timestamp: int

    def __str__(self):
        return f'{self.userId}, {self.movieId}, {self.tag}, {self.timestamp}'