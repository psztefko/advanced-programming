from movie import Movie

from typing import List
import pandas as pd
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

def read_excel_rows() -> List[Movie]:
    df = pd.read_csv("movies.csv")
    list_of_movies = []
    for index, row in df.iterrows():
        list_of_movies.append(Movie(row[0], row[1], row[2]))
    return list_of_movies


class Movies(Resource):
    def get(self):
        return [movie.__dict__ for movie in read_excel_rows()]

api.add_resource(Movies, '/')

if __name__ == '__main__':
    app.run(debug=True)
