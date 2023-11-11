from pymongo import MongoClient as MC, ASCENDING, DESCENDING
from config import MONGODB_CONNECTION_STRING, DATABASE_NAME
from datetime import datetime


def GetAllRecords(sortField: str):
    records = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        records = db["records"].find()
        records = records.sort([(sortField, ASCENDING)])

    except Exception as e:
        print(f"An error occurred: {e}")

    return records


def GetAllRecordsByArtist(artistid: int):
    records = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        records = db["records"].find({"artistid": artistid})
        records = records.sort([("recorded", ASCENDING)])

    except Exception as e:
        print(f"An error occurred: {e}")

    return records


def GetArtistRecords(artistid: int):
    records = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        records = (
            db["records"].find({"artistid": artistid}).sort([("recorded", DESCENDING)])
        )
    except Exception as e:
        print(f"An error occurred: {e}")

    return records


def GetRecordsByYear(year: int):
    records = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        records = db["records"].find({"recorded": year}).sort([("artistid", ASCENDING)])
    except Exception as e:
        print(f"An error occurred: {e}")

    return records


def GetRecordIds():
    recordIdList = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        recordsCollection = db["records"]

        recordIdList = recordsCollection.distinct("recordid")
    except Exception as e:
        print(f"An error occurred: {e}")

    return recordIdList


def AddNewRecord(document):
    _id = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        _id = db["records"].insert_one(document)
    except Exception as e:
        print(f"An error occurred: {e}")

    return _id.inserted_id


def GetRecordById(recordid: int):
    record = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        record = db["records"].find_one({"recordid": recordid})
    except Exception as e:
        print(f"An error occurred: {e}")

    return record


def CheckIfRecordExists(recordid: int) -> bool:
    exists = False

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        record = db["records"].find_one({"recordid": recordid})

        if record:
            exists = True

    except Exception as e:
        print(f"An error occurred: {e}")

    return exists


def UpdateRecord(query, newValues):
    affected = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        result = db["records"].update_one(query, newValues)

        if result:
            affected = result.modified_count

    except Exception as e:
        print(f"An error occurred: {e}")

    return affected


def DeleteRecord(query: str) -> int:
    affected = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        result = db["records"].delete_one(query)

        if result:
            affected = result.deleted_count

    except Exception as e:
        print(f"An error occurred: {e}")

    return affected


def GetRecordsByName(query):
    records = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        condition = query
        records = db["records"].find(
            condition,
        )

    except Exception as e:
        print(f"An error occurred: {e}")

    return records


def GetTotalNumberOfCDs():
    total = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        pipeline = [
            {
                "$match": {
                    "media": "CD",
                },
            },
            {
                "$group": {
                    "_id": None,  # Use None to group all matching records together
                    "totalDiscs": {"$sum": "$discs"},  # Sum the 'discs' field
                }
            },
        ]

        result = list(db["records"].aggregate(pipeline))

        if result:
            total = result[0]["totalDiscs"]
    except Exception as e:
        print(f"An error occurred: {e}")

    return total


def GetTotalNumberOfCdDvds():
    total = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        pipeline = [
            {
                "$match": {
                    "media": "CD/DVD",
                },
            },
            {
                "$group": {
                    "_id": None,  # Use None to group all matching records together
                    "totalDiscs": {"$sum": "$discs"},  # Sum the 'discs' field
                }
            },
        ]

        result = list(db["records"].aggregate(pipeline))

        if result:
            total = result[0]["totalDiscs"]
    except Exception as e:
        print(f"An error occurred: {e}")

    return total


def GetTotalNumberIfCdBlurays():
    total = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        pipeline = [
            {
                "$match": {
                    "media": "CD/Blu-ray",
                },
            },
            {
                "$group": {
                    "_id": None,  # Use None to group all matching records together
                    "totalDiscs": {"$sum": "$discs"},  # Sum the 'discs' field
                }
            },
        ]

        result = list(db["records"].aggregate(pipeline))

        if result:
            total = result[0]["totalDiscs"]
    except Exception as e:
        print(f"An error occurred: {e}")

    return total


def GetTotalNumberOfRecords():
    total = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        pipeline = [
            {
                "$match": {
                    "media": "R",
                },
            },
            {
                "$group": {
                    "_id": None,  # Use None to group all matching records together
                    "totalDiscs": {"$sum": "$discs"},  # Sum the 'discs' field
                }
            },
        ]

        result = list(db["records"].aggregate(pipeline))

        if result:
            total = result[0]["totalDiscs"]
    except Exception as e:
        print(f"An error occurred: {e}")

    return total


def GetTotalNumberOfDVDs():
    total = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        pipeline = [
            {
                "$match": {
                    "media": "DVD",
                },
            },
            {
                "$group": {
                    "_id": None,  # Use None to group all matching records together
                    "totalDiscs": {"$sum": "$discs"},  # Sum the 'discs' field
                }
            },
        ]

        result = list(db["records"].aggregate(pipeline))

        if result:
            total = result[0]["totalDiscs"]
    except Exception as e:
        print(f"An error occurred: {e}")

    return total


def GetTotalNumberOfBlurays():
    total = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        pipeline = [
            {
                "$match": {
                    "media": "Blu-ray",
                },
            },
            {
                "$group": {
                    "_id": None,  # Use None to group all matching records together
                    "totalDiscs": {"$sum": "$discs"},  # Sum the 'discs' field
                }
            },
        ]

        result = list(db["records"].aggregate(pipeline))

        if result:
            total = result[0]["totalDiscs"]
    except Exception as e:
        print(f"An error occurred: {e}")

    return total


def GetTotalNumberOfDiscs():
    total = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        pipeline = [
            {
                "$group": {
                    "_id": None,  # Use None to group all matching records together
                    "totalDiscs": {"$sum": "$discs"},  # Sum the 'discs' field
                }
            },
        ]

        result = list(db["records"].aggregate(pipeline))

        if result:
            total = result[0]["totalDiscs"]
    except Exception as e:
        print(f"An error occurred: {e}")

    return total


def GetArtistNumberOfRecords(artistid):
    total = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        pipeline = [
            {
                "$match": {
                    "artistid": artistid,
                },
            },
            {
                "$group": {
                    "_id": None,  # Use None to group all matching records together
                    "totalDiscs": {"$sum": "$discs"},  # Sum the 'discs' field
                }
            },
        ]

        result = list(db["records"].aggregate(pipeline))

        if result:
            total = result[0]["totalDiscs"]
    except Exception as e:
        print(f"An error occurred: {e}")

    return total


def GetBoughtDates() -> list:
    dates = []

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        records = db["records"].find()

        for record in records:
            date = rd.ChangeDate(record["bought"])
            dates.append()
    except Exception as e:
        print(f"An error occurred: {e}")

    return dates


def GetDiscCountForYear(year):
    total = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        pipeline = [
            {
                "$match": {
                    "recorded": year,
                },
            },
            {
                "$group": {
                    "_id": None,  # Use None to group all matching records together
                    "totalDiscs": {"$sum": "$discs"},  # Sum the 'discs' field
                }
            },
        ]

        result = list(db["records"].aggregate(pipeline))

        if result:
            total = result[0]["totalDiscs"]
    except Exception as e:
        print(f"An error occurred: {e}")

    return total


def GetBoughtDiscCountForYear(year: int) -> int:
    totalDiscs = 0

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        pipeline = [
            {
                "$match": {
                    "$expr": {
                        "$eq": [
                            {"$year": {"$dateFromString": {"dateString": "$bought"}}},
                            year,
                        ]
                    }
                }
            },
            {
                "$group": {
                    "_id": None,
                    "totalDiscs": {"$sum": "$discs"},
                }
            },
        ]

        result = list(db["records"].aggregate(pipeline))

        if result:
            totalDiscs = result[0]["totalDiscs"]
    except Exception as e:
        print(f"An error occurred: {e}")

    return totalDiscs


def GetNoRecordReview():
    records = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        filterCondition = {"review": {"$eq": ""}}
        records = db["records"].find(filterCondition, {"review": 0})
        records = records.sort(("artistid", ASCENDING), [("recorded", ASCENDING)])

    except Exception as e:
        print(f"An error occurred: {e}")

    return records


def GetNoReviewCount():
    total = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        pipeline = [
            {
                "$match": {
                    "review": "",
                },
            },
            {
                "$group": {
                    "_id": None,  # Use None to group all matching records together
                    "totalDocuments": {"$sum": 1},  # Sum the number of documents
                }
            },
        ]

        result = list(db["records"].aggregate(pipeline))

        if result:
            total = result[0]["totalDocuments"]
    except Exception as e:
        print(f"An error occurred: {e}")

    return total


def GetTotalArtistCostById(artistid: int) -> float:
    totalCost = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        pipeline = [
            {
                "$match": {
                    "artistid": artistid,
                },
            },
            {
                "$group": {
                    "_id": None,  # Use None to group all matching records together
                    "totalCost": {"$sum": "$cost"},  # Sum the 'cost' field
                },
            },
        ]

        result = list(db["records"].aggregate(pipeline))

        if result:
            totalCost = result[0]["totalCost"]
    except Exception as e:
        print(f"An error occurred: {e}")

    return totalCost


def GetTotalArtistCost():
    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        pipeline = [
            {
                "$group": {
                    "_id": "$artistid",
                    "Name": {
                        "$first": {
                            "$concat": [
                                {"$ifNull": ["$firstname", ""]},
                                " ",
                                {"$ifNull": ["$lastname", ""]},
                            ]
                        }
                    },
                    "TotalDiscs": {"$sum": "$discs"},
                    "TotalCost": {"$sum": "$cost"},
                }
            },
            {
                "$project": {
                    "_id": 0,  # Exclude the _id field from the output
                    "ArtistId": "$_id",
                    "Name": "$Name",
                    "TotalDiscs": "$TotalDiscs",
                    "TotalCost": "$TotalCost",
                }
            },
            {"$sort": {"TotalCost": -1}},
        ]

        results = list(db["records"].aggregate(pipeline))
    except Exception as e:
        print(f"An error occurred: {e}")

    return results
