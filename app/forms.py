from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators

class LoginForm(FlaskForm):
    username = StringField('USERNAME', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.Length(min=4, max=35)])
    submit =  SubmitField("Sign in")
    remember_me = BooleanField("Remember Me")

class RecipeForm(FlaskForm):
    user_id = StringField("ID Number", validators=[validators.DataRequired()])
    title = StringField("Title", validators=[validators.Length(min=1, max=80)])
    description = StringField("Description", validators=[validators.DataRequired()])
    ingredients = StringField("Ingredients", validators=[validators.DataRequired()])
    instructions = StringField("Instructions", validators=[validators.DataRequired()])
    submit_recipe =  SubmitField("submit recipe")

