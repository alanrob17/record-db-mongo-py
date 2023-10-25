import pymongo


def updateDoc(client, condition, operation):
    db = client["record-db"]
    collection = db["records"]
    results = collection.update_many(condition, operation)

    print(results.modified_count)


client = pymongo.MongoClient("mongodb://localhost:27017")

condition = {"name": {"$eq": "I Can't Make You Love Me (ep)"}}
operation = {"$set": {"name": "I Can't Make You Love Me (EP)"}}

updateDoc(client, condition, operation)
