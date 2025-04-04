from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password = db.Column(db.String(32))
    email = db.Column(db.String(32))


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(80))
    description = db.Column(db.String())
    ingredients = db.Column(db.String())
    instructions = db.Column(db.String())
    created = db.Column(db.String())

    def __repr__(self):
        # Represents the recipe with user id, title, and recipe id
        return f'user {self.user_id} made post {self.title}, post ID: {self.id}'
