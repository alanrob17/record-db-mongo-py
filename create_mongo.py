from pymongo import MongoClient


def createMany(client, documents):
    db = client["TestDB"]
    collection = db["Test"]
    collection.insert_many(documents)


client = MongoClient("mongodb://localhost:27017")

documents = [
    {"id": 24, "item": "Soy Latte", "size": "Short", "quantity": 22},
    {"id": 25, "item": "Double Latte", "size": "Long", "quantity": 12},
    {"id": 26, "item": "Cappuccino", "size": "Long", "quantity": 42},
    {"id": 27, "item": "Soy Flat White", "size": "Short", "quantity": 25},
    {"id": 28, "item": "Americano", "size": "Short", "quantity": 34},
]

createMany(client, documents)
