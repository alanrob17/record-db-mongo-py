import pymongo


def createMany(client, documents):
    db = client["TestDB"]
    collection = db["Test"]
    collection.insert_many(documents)


client = pymongo.MongoClient("mongodb://localhost:27017")

documents = [
    {"id": 19, "item": "Soy Latte", "size": "Short", "quantity": 22},
    {"id": 20, "item": "Double Latte", "size": "Long", "quantity": 12},
    {"id": 21, "item": "Cappuccino", "size": "Long", "quantity": 42},
    {"id": 22, "item": "Mocha", "size": "Short", "quantity": 25},
    {"id": 23, "item": "Americano", "size": "Short", "quantity": 34},
]

createMany(client, documents)
