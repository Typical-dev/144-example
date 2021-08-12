from flask import Flask, json, jsonify, request
import csv
from storage import all_movies, liked_movie, disliked_movie, notwatched
from demographic_filtering import output
from content_filtering import get_recommendation
app = Flask(__name__)
@app.route("/get-movie")
def get_movie():
    return jsonify({"data":all_movies[0], "status": "success"})
@app.route("/liked-movies", methods = ["POST"])
def liked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movie.append(movie)
    return jsonify({"status", "success"}), 201

@app.route("/disliked-movies", methods = ["POST"])
def disliked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    disliked_movie.append(movie)
    return jsonify({"status", "success"}), 201

@app.route("/notwatched", methods = ["POST"])
def notwatched():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    notwatched.append(movie)
    return jsonify({"status", "success"}), 201
@app.route("/popular-movies")
def popular_movies():
    movie_data = []
    for movie in output:
        _d = {"title":movie[0],
        "poster_link":movie[1],
        "release_date":movie[2] or "n/a",
        "duration":movie[3],
        "rating":movie[5],
        "overview":movie[6]
        }
        
        movie_data.append(_d)
    return jsonify({"data":movie_data, "status":"success"}), 200
@app.route("/recommended-movies")
def recommended_movies():
    all_recommended = []
    for movie in liked_movie:
        output = get_recommendation(liked_movie[19])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended, _ in itertools.groupby(all_recommended))
    movie_data = []
    for recommended in all_recommended:
        _d = {"title":movie[0],
        "poster_link":movie[1],
        "release_date":movie[2] or "n/a",
        "duration":movie[3],
        "rating":movie[5],
        "overview":movie[6]
        }

        movie_data.append(_d)
    return jsonify({"data": movie_data, "status": "success"}), 200

if(__name__) == "__main__":
    app.run()