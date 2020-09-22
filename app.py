import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'FoodRecipes'
app.config["MONGO_URI"] = 'mongodb+srv://sonia:candy1991@myfirstproject.jnu5z.mongodb.net/FoodRecipes?retryWrites=true&w=majority'


mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipe')
def get_recipes():
    data = []


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
