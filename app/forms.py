from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.fields.simple import TextAreaField


class RecipeForm(FlaskForm):
    title = StringField("Title", validators=[validators.Length(min=1, max=80)])
    description = TextAreaField("Description", validators=[validators.DataRequired()])
    ingredients = TextAreaField("Ingredients", validators=[validators.DataRequired()])
    instructions = TextAreaField("Instructions", validators=[validators.DataRequired()])
    submit_recipe =  SubmitField("submit recipe")

