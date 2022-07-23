from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")
connection_string = f"mongodb+srv://danielfr500:{password}@firstmongo.chjgl.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)

dbs = client.list_database_names()  # check list of dbs
print(dbs)

test_db = client.test  # Access db
collections = test_db.list_collection_names()  # access collection lists
print(collections)


# CRUD

# Create
def insert_test_document():
    # get access to test collection from test database using .notation
    collection = test_db.test
    test_document = {
        "name": "Tim",
        "type": "Test"
    }
    # inserts one document into a collection
    inserted_id = collection.insert_one(test_document).inserted_id
    print(inserted_id)


insert_test_document()

# if trying to access a db that doesn't exist - mongdb will create it
production = client.production
person_collection = production.person_collection


def create_documents():
    first_names = ["Tim", "Sarah", "Jennifer", "Jose", "Brad", "Allen"]
    last_names = ["Ruscica", "Smith", "Bart", "Cater", "Pit", "Geral"]
    ages = [21, 40, 23, 19, 34, 67]

    for first_name, last_name, age in zip(first_names, last_names, age):
        doc = {"first_name": first_name, "last_name":last_name, "age":age}
        person_collection.insert_one(doc)