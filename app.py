import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipe_Collections'
app.config["MONGO_URI"] =  os.getenv("MONGO_URI", 'mongodb://localhost')

mongo = PyMongo(app)

# for all the recipes collected
@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())



@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", origin=mongo.db.origin.find(), categories=mongo.db.categories.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to.dict())
    return redirect(url_for('get_recipes'))

# this fuction help to edith already inputed date from the database

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    all_origin = mongo.db.origin.find()
    return render_template('editrecipe.html', recipe=the_recipe, categories=all_categories, origin=all_origin)

# the fuction updates the database with new information
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)})
    {
        'recipe_name': request.form.get('recipe_name'),
        'origin_name': request.form.get('origin_name'),
        'category_name': request.form.get('category_name'),
        'ingredients': request.form.get('ingredients'),
        'recipe_descriptions': request.form.get('recipe_descriptions'),
        'require_tools': request.form.get('require_tools'),
        'full_name': request.form.get('full_name'),
        'email': request.form.get('email'),
        'date': request.form.get('date'),
        'i_certify': request.form.get('i_certify')
        }
    return redirect(url_for('get_recipes'))

# this function helps to delete already inputed database
@app.route('/delete_recipe/<recipe_id>', methods=["GET", "POST"])
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

@app.route('/tools', methods=["POST", "GET"])
def tools():
    return render_template('tools.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)

