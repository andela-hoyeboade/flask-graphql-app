from graphene import ID, Field, Int, List, ObjectType, Schema, String
from models import Entry, User


class EntryType(ObjectType):
    id = Int()
    name = String()


class UserType(ObjectType):
    id = Int()
    username = String()
    entries = List(EntryType)


class RootQuery(ObjectType):
    entry = Field(EntryType, id=Int(), name=String())
    user = Field(UserType, username=String())

    def resolve_entry(self, args, context, info):
        return Entry.query.filter_by(**args).first()

    def resolve_user(self, args, context, info):
        return User.query.filter_by(**args).first()
