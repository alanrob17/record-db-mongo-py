from pymongo import MongoClient

"""
test routines for MongoDB
"""

client = MongoClient("mongodb://localhost:27017")

db = client["Test"]

collection = db["customers"]

## --------------------------------------------

# collection.drop()

## --------------------------------------------

# documents = collection.delete_many({})

# print(f"{documents.deleted_count} documents deleted.")

## --------------------------------------------

# # Limit no. of documents returned
# results = collection.find().limit(5)

# for document in results:
#     print(document)

## --------------------------------------------

# query = { "address": { "$regex": "^P" } }
# new_values = { "$set": { "name": "Minnie" } }

# documents = collection.update_many(query, new_values)

# print(f"{documents.modified_count} documents updated.")

## --------------------------------------------

# query = { "address": "Valley 345" }
# new_values = { "$set": { "address": "Canyon 123" } }

# collection.update_one(query, new_values)

# #print "customers" after the update:
# for customer in collection.find():
#   print(customer)

## --------------------------------------------

# query = {"address": {"$regex": "^S"}}

# results = collection.delete_many(query)

# print(results.deleted_count)

## --------------------------------------------

# query = {"address": "Green Grass 1"}

# result = collection.delete_one(query)

# print(result.deleted_count)

## --------------------------------------------

# documents = collection.find().sort("name", -1)

# for document in documents:
#     print(document)

## --------------------------------------------

# documents = collection.find().sort("name")

# for document in documents:
#     print(document)

## --------------------------------------------

# query = {"address": {"$regex": "^S"}}

# documents = collection.find(query)

# for document in documents:
#     print(document)

## --------------------------------------------

# query = {"address": {"$gt": "S"}}

# documents = collection.find(query)

# for document in documents:
#     print(document)

## --------------------------------------------

# query = {"address": "Park Lane 38"}

# documents = collection.find(query)

# for document in documents:
#     print(document)

## --------------------------------------------

# filter_condition = {"name": {"$eq": "Alan"}}

# # don't print the email field
# for customer in collection.find(filter_condition, {"email": 0}):
#     print(customer)

# customers = db["customers"].find()

# for customer in customers:
#     print(customer)

## --------------------------------------------

# for customer in collection.find({}, {"_id": 0, "name": 1, "address": 1}):
#     print(customer)

## --------------------------------------------

# documents = [
#     {"_id": 1, "name": "John", "address": "Highway 37"},
#     {"_id": 2, "name": "Peter", "address": "Lowstreet 27"},
#     {"_id": 3, "name": "Amy", "address": "Apple st 652"},
#     {"_id": 4, "name": "Hannah", "address": "Mountain 21"},
#     {"_id": 5, "name": "Michael", "address": "Valley 345"},
#     {"_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
#     {"_id": 7, "name": "Betty", "address": "Green Grass 1"},
#     {"_id": 8, "name": "Richard", "address": "Sky st 331"},
#     {"_id": 9, "name": "Susan", "address": "One way 98"},
#     {"_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
#     {"_id": 11, "name": "Ben", "address": "Park Lane 38"},
#     {"_id": 12, "name": "William", "address": "Central st 954"},
#     {"_id": 13, "name": "Chuck", "address": "Main Road 989"},
#     {"_id": 14, "name": "Viola", "address": "Sideway 1633"},
# ]

# results = collection.insert_many(documents)

# print(results.inserted_ids)

## --------------------------------------------

# documents = [
#     {"name": "Amy", "address": "Apple st 652", "email": "amy@amy.com"},
#     {"name": "Hannah", "address": "Mountain 21", "email": "Hannah@Hannah.com"},
#     {"name": "Michael", "address": "Valley 345", "email": "Michael@Michael.com"},
#     {"name": "Sandy", "address": "Ocean blvd 2", "email": "Sandy@Sandy.com"},
#     {"name": "Betty", "address": "Green Grass 1", "email": "Betty@Betty.com"},
#     {"name": "Richard", "address": "Sky st 331", "email": "amy@amy.com"},
#     {"name": "Susan", "address": "One way 98", "email": "Richard@Richard.com"},
#     {"name": "Vicky", "address": "Yellow Garden 2", "email": "Vicky@Vicky.com"},
#     {"name": "Ben", "address": "Park Lane 38", "email": "ben@ben.com"},
#     {"name": "William", "address": "Central st 954", "email": "William@William.com"},
#     {"name": "Chuck", "address": "Main Road 989", "email": "Chuck@Chuck.com"},
#     {"name": "Viola", "address": "Sideway 1633", "email": "Viola@Viola.com"},
# ]

# results = collection.insert_many(documents)

# print(results)

# customers = db["customers"].find()

# for customer in customers:
#     print(customer)

## --------------------------------------------

# dictionary = {"name": "Ethan", "address": "Highway 38", "email": "ethan@ethan.com"}

# result = collection.insert_one(dictionary)

# print(result.inserted_id)

# print(db.list_collection_names())

# customers = db["customers"].find()

# for customer in customers:
#     print(customer)

# collection_list = db.list_collection_names()
# collection = "artists"
# if collection in collection_list:
#     print(f"The {collection} collection exists.")
# else:
#     print(f"The {collection} collection doesn't exist.")
