import pymongo


def deleteDocument(client, condition):
    db = client["TestDB"]
    collection = db["Test"]
    results = collection.delete_many(condition)

    print(results.deleted_count)


client = pymongo.MongoClient("mongodb://localhost:27017")

condition = {"id": {"$eq": 21}}

deleteDocument(client, condition)
