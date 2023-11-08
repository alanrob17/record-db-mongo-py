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


# def GetArtistsForYear(year):
