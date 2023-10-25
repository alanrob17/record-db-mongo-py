import pymongo


def readDocuments(client, condition):
    db = client["record-db"]
    collection = db["records"]
    records = collection.find(condition)

    for record in records:
        print(f"{record['recorded']} - {record['name']} ({record['media']})")


client = pymongo.MongoClient("mongodb://localhost:27017")

# condition = {"name": {"$eq": "Blonde On Blonde"}}
condition = {"name": {"$regex": ".*blonde.*", "$options": "i"}}

readDocuments(client, condition)
