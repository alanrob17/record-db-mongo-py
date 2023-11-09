from pymongo import MongoClient as MC, ASCENDING, DESCENDING
from config import MONGODB_CONNECTION_STRING, DATABASE_NAME


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
