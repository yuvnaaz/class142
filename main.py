from flask import Flask,jsonify,request
import csv

allmovies = []
with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    allmovies = data[1:]
liked_movies = []
not_liked_movies = []
didnotwatch = []
app = Flask(_name_)
@app.route('/get-movie')
def get-movie():
    return jsonify({
        'data': allmovies[0],
        'status': 'success',
    })
@app.route('/liked-movies', methods = ['POST'])
def liked_movie():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    liked_movies.append(movie)
    return jsonify({
        'status': 'success', 
    }),201
@app.route('/not_liked_movies', methods = ["POST"])
def not_liked_movies():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    not_liked_movies.append(movie)
    return jsonify({
        'status': 'success',
    }),201
@app.route('/didnotwatch', methods = ['POST'])
def didnotwatch():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    didnotwatch.append(movie)
    return jsonify({
        'status': 'success',
    }),201
if _name_ == '_main_':
    app.run()