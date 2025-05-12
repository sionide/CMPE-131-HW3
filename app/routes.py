import datetime
from app import myapp_obj
from flask import render_template, session
from flask import redirect
from app.forms import RecipeForm
from app.models import Recipe
from app import db
from sqlalchemy import select
# from <X> import <Y>

@myapp_obj.route("/")
def main():
    name = "Have a nice day!"
    return render_template("hello.html", name=name)

@myapp_obj.route("/recipe/new", methods=['GET', 'POST'])
def create_recipe():
    form = RecipeForm()
    if form.validate_on_submit(): # Checks if user input is valid
        # Creates a recipe
        recipe = Recipe(title=form.title.data,
                        user_id=form.user_id.data,
                        description=form.description.data,
                        ingredients=form.ingredients.data,
                        instructions=form.instructions.data,
                        created=datetime.datetime.now())

        # Adds a recipe to the database
        db.session.add(recipe)
        db.session.commit()
        return redirect("/")
    else:
        # User has invalid input
        print("MOOOO MOOO BAD")
    return render_template("recipe_new.html", form=form)

@myapp_obj.route("/recipes")
def show_all_recipes():
    all_recipes = Recipe.query.all()
    return render_template("show_all_recipes.html", all_recipes=all_recipes)

@myapp_obj.route("/recipe/<string:recipe_id>")
def load_recipe(recipe_id):
    # Finds a recipe based on the recipe's id
    filter = select(Recipe).where(Recipe.id == int(recipe_id))
    recipe = db.session.execute(filter).scalars().first()
    return render_template("load_recipe.html", recipe=recipe)

@myapp_obj.route("/recipe/<string:recipe_id>/delete")
def delete_recipe(recipe_id):
    # Finds a recipe based on the recipe's id
    filter = select(Recipe).where(Recipe.id == int(recipe_id))
    recipe = db.session.execute(filter).scalars().first()

    # Delete recipe from database
    db.session.delete(recipe)
    db.session.commit()
    return f"{recipe.title} has been deleted"