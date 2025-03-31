import datetime
from app import myapp_obj
from flask import render_template
from flask import redirect
from app.forms import LoginForm, RecipeForm
from app.models import User, Recipe
from app import db
# from <X> import <Y>

@myapp_obj.route("/")
def main():
    name = "carlos"
    return render_template("hello.html", name=name)

@myapp_obj.route("/accounts")
def users():
    return "My USER ACCOUNTS"

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(f"Here is the input from the user {form.username.data} and {form.password.data}")
        user = User(username=form.username.data, password=form.password.data)

        db.session.add(user)
        db.session.commit()
        return redirect("/")
    else:
        print("MOOOO MOOO BAD")
    return render_template("login.html", form=form)
    # What is render template returning?
    #return str(type(render_template("login.html", form=form)))

@myapp_obj.route("/recipe/new", methods=['GET', 'POST'])
def create_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        print(f"Here is the input from the user {form.title.data}")
        recipe = Recipe(title=form.title.data,
                        user_id=form.user_id.data,
                        description=form.description.data,
                        ingredients=form.ingredients.data,
                        instructions=form.instructions.data,
                        created=datetime.datetime.now())

        db.session.add(recipe)
        db.session.commit()
        return redirect("/")
    else:
        print("MOOOO MOOO BAD")
    return render_template("recipe_new.html", form=form)