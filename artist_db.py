from pymongo import MongoClient as MC, ASCENDING, DESCENDING
from config import MONGODB_CONNECTION_STRING, DATABASE_NAME


def GetAllArtists():
    artists = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        artists = db["artists"].find()
        artists = artists.sort([("lastname", ASCENDING), ("firstname", ASCENDING)])

    except Exception as e:
        print(f"An error occurred: {e}")

    return artists


def GetArtistByName(artistName: str) -> tuple:
    artist = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        artist = db["artists"].find_one({"name": artistName})

    except Exception as e:
        print(f"An error occurred: {e}")

    return artist


def GetArtistIds():
    artistIdList = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        artistsCollection = db["artists"]

        artistIdList = artistsCollection.distinct("artistid")
    except Exception as e:
        print(f"An error occurred: {e}")

    return artistIdList


def CheckIfArtistExists(name: str) -> bool:
    exists = False

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        artist = db["artists"].find_one({"name": name})

        if artist:
            exists = True

    except Exception as e:
        print(f"An error occurred: {e}")

    return exists


def AddNewArtist(document):
    _id = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        _id = db["artists"].insert_one(document)
    except Exception as e:
        print(f"An error occurred: {e}")

    return _id.inserted_id


def CheckIfArtistIdExists(artistid: int) -> bool:
    exists = False

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        artistid = db["artists"].find_one({"artistid": artistid})

        if artistid:
            exists = True

    except Exception as e:
        print(f"An error occurred: {e}")

    return exists


def UpdateArtist(query, newValues):
    affected = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        result = db["artists"].update_one(query, newValues)

        if result:
            affected = result.modified_count

    except Exception as e:
        print(f"An error occurred: {e}")

    return affected


def DeleteArtist(query: str) -> int:
    affected = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        result = db["artists"].delete_one(query)

        if result:
            affected = result.deleted_count

    except Exception as e:
        print(f"An error occurred: {e}")

    return affected


def GetArtistById(artistid: int) -> tuple:
    artist = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        artist = db["artists"].find_one({"artistid": artistid})

    except Exception as e:
        print(f"An error occurred: {e}")

    return artist


def GetBiography(artistid: int) -> str:
    biography = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        artist = db["artists"].find_one({"artistid": artistid})
        biography = artist["biography"]

    except Exception as e:
        print(f"An error occurred: {e}")

    return biography


def GetArtistIdByNames(firstName: str, lastName: str) -> int:
    artistid = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        artist = db["artists"].find_one({"firstname": firstName, "lastname": lastName})
        artistid = artist["artistid"]

    except Exception as e:
        print(f"An error occurred: {e}")

    return artistid


def GetArtistsWithNoBio():
    artists = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        filterCondition = {"biography": {"$eq": ""}}
        artists = db["artists"].find(filterCondition, {"biography": 0})
        artists = artists.sort([("lastname", ASCENDING), ("firstname", ASCENDING)])

    except Exception as e:
        print(f"An error occurred: {e}")

    return artists


def GetNoBiographyCount():
    count = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        filterCondition = {"biography": ""}
        count = db["artists"].count_documents(filterCondition)
    except Exception as e:
        print(f"An error occurred: {e}")

    return count


def GetArtistName(artistid: str) -> str:
    artistName = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        artist = db["artists"].find_one({"artistid": artistid})
        artistName = artist["name"]
    except Exception as e:
        print(f"An error occurred: {e}")

    return artistName


def GetMongoId(artistid):
    mongoId = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        artist = db["artists"].find_one({"artistid": artistid})
        mongoId = artist["_id"]
    except Exception as e:
        print(f"An error occurred: {e}")

    return mongoId


def GetArtistByPartialName(query: str):
    artists = None

    try:
        client = MC(MONGODB_CONNECTION_STRING)
        db = client[DATABASE_NAME]

        condition = query
        artists = db["artists"].find(
            condition,
        )
    except Exception as e:
        print(f"An error occurred: {e}")

    return artists
