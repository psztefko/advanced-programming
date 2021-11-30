from src.movie import Movie
from src.link import Link
from src.rating import Rating
from src.tag import Tag

from typing import List
import pandas as pd
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

def get_movies() -> List[Movie]:
    df = pd.read_csv("lab_7/src/files/movies.csv")
    list_of_movies = []
    for index, row in df.iterrows():
        list_of_movies.append(Movie(row[0], row[1], row[2]))
    return list_of_movies

def get_links() -> List[Link]:
    df = pd.read_csv("lab_7/src/files/links.csv")
    list_of_links = []
    for index, row in df.iterrows():
        list_of_links.append(Link(row[0], row[1], row[2]))
    return list_of_links

def get_rating() -> List[Rating]:
    df = pd.read_csv("lab_7/src/files/ratings.csv")
    list_of_ratings = []
    for index, row in df.iterrows():
        list_of_ratings.append(Link(row[0], row[1], row[2], row[3]))
    return list_of_ratings

def get_tags() -> List[Rating]:
    df = pd.read_csv("lab_7/src/files/ratings.csv")
    list_of_ratings = []
    for index, row in df.iterrows():
        list_of_ratings.append(Link(row[0], row[1], row[2], row[3]))
    return list_of_ratings

class Movies(Resource):
    def get(self):
        return [movie.__dict__ for movie in get_movies()]

class Links(Resource):
    def get(self):
        return [link.__dict__ for link in get_links()]

class Ratings(Resource):
    def get(self):
        return [rating.__dict__ for rating in get_rating()]

class Tags(Resource):
    def get(self):
        return [tag.__dict__ for tag in get_tags()]


api.add_resource(Movies, '/movies')

api.add_resource(Links, '/links')

api.add_resource(Ratings, '/rating')

api.add_resource(Tags, '/tags')


if __name__ == '__main__':
    app.run(debug=True)
