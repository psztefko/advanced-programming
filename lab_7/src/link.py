from dataclasses import dataclass


@dataclass
class Link:

    movieId: int
    imdbId: int
    tmdbId: int

    def __str__(self):
        return f'{self.movieId}, {self.imdbId}, {self.tmdbId}'