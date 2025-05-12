# CMPE-131-HW3
How I set up my environment

Using bash terminal:
    
set up virutal environment:

    python -m venv venv
    source venv/Scripts/activate

install libraries from requirements.txt:

    pip install -r requirements.txt

Run this command from the root of the project:

    python .\run.py

To navigate to the "All Recipes" Page, go to http://127.0.0.1:5000/recipes
The recipes are formatted as:

    id: [id number], [title]

To create a recipe, go to http://127.0.0.1:5000/recipe/new and fill out the form
Upon clicking submit and successfully creating a recipe, you will redirected to the "All Recipes" page, otherwise continue filling out the form


To go to a specific recipe, append the recipe id to the end of http://127.0.0.1:5000/recipe/

Examples:
    http://127.0.0.1:5000/recipe/[insert_recipe_id_here]/
    
    http://127.0.0.1:5000/recipe/1/

To delete a specific recipe, append the word "delete" to the end of a recipe's URL

Examples:
    http://127.0.0.1:5000/recipe/[insert_recipe_id_here]/delete/
    
    http://127.0.0.1:5000/recipe/1/delete/