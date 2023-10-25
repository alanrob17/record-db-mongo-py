import pymongo

"""
CRUD routines in MongoDB
"""


def createMany(client, documents):
    db = client["TestDB"]
    collection = db["Test"]
    collection.insert_many(documents)


def readDocuments(client, condition):
    db = client["TestDB"]
    collection = db["Test"]
    results = collection.find(condition)

    for row in results:
        print(row)


def updateDoc(client, condition, operation):
    db = client["TestDB"]
    collection = db["Test"]
    results = collection.update_many(condition, operation)

    print(results.modified_count)


def deleteDocument(client, condition):
    db = client["TestDB"]
    collection = db["Test"]
    results = collection.delete_many(condition)

    print(results.deleted_count)


client = pymongo.MongoClient("mongodb://localhost:27017")

documents = [
    {"id": 11, "item": "Americanos", "size": "Short", "quantity": 22},
    {"id": 12, "item": "Latte", "size": "Long", "quantity": 12},
    {"id": 13, "item": "Cappuccino", "size": "Long", "quantity": 42},
    {"id": 14, "item": "Mocha", "size": "Short", "quantity": 25},
    {"id": 15, "item": "Americanos", "size": "Short", "quantity": 34},
]

# createMany(client, documents)

condition = {"item": {"$eq": "Latte"}}

readDocuments(client, condition)

condition = {"item": {"$eq": "Americanos"}}
operation = {"$set": {"item": "Americano"}}
# updateDoc(client, condition, operation)

condition = {"id": {"$eq": 15}}
# deleteDocument(client, condition)
