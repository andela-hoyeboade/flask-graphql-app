import contentful
from app import app
from flask import jsonify
from flask_graphql import GraphQLView
from graphene import Schema
from models import Entry, User
from schema import RootQuery


def create_user():
    if not User.query.filter_by(username='hassan').first():
        new_user = User(username='hassan',
                        email='hassan@gmail.com', password='hassan')
        new_user.save()


def create_new_entry(entry, user_id):
    new_entry = Entry(name=entry.name, creator_id=user_id)
    new_entry.save()


def update_existing_entries(entries, user_id):
    for entry in entries:
        if not Entry.query.filter_by(name=entry.name, creator_id=user_id):
            create_new_entry(entry)


@app.route('/')
def index():
    return jsonify({"message": "Welcome, Please visit /graphql to access the graphql interface"})


@app.route('/api/entries/update', methods=["GET"])
def update_entries():
    # Ensure user is created
    create_user()

    # Define  Credentials

    SPACE_ID = 'cfexampleapi'
    ACCESS_TOKEN = 'b4c0n73n7fu1'

    # Create Contentful Delivery API Client

    client = contentful.Client(SPACE_ID, ACCESS_TOKEN)

    entries = client.entries()

    user_id = User.query.filter_by(username='hassan').first().id

    if not Entry.query.all():
        for entry in entries:
            create_new_entry(entry, user_id)
    else:
        update_existing_entries(entries, user_id)
    return jsonify({"message": "Content updated"})

app.add_url_rule(
    '/graphql', view_func=GraphQLView.as_view('graphql', schema=Schema(query=RootQuery), graphiql=True, context={}))
