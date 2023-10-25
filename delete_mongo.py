from pymongo import MongoClient


def deleteDocument(client, condition):
    db = client["TestDB"]
    collection = db["Test"]
    results = collection.delete_many(condition)

    print(results.deleted_count)


client = MongoClient("mongodb://localhost:27017")

condition = {"id": {"$eq": 28}}

deleteDocument(client, condition)
