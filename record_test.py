from pymongo import MongoClient as MC, ASCENDING
from config import MONGODB_CONNECTION_STRING, DATABASE_NAME
import artist_db as a
import artist_data as ad
import record_db as r
import record_data as rd


def GetArtistAndAlbums(artistName: str):
    artist = a.GetArtistByName(artistName)

    if artist:
        artistid = artist["artistid"]
    else:
        print(f"Artist '{artistName}' not found in the 'artists' collection.")
        artistid = None

    if artistid is not None:
        records = r.GetArtistRecords(artistid)

        albumNames = [
            [record["name"], record["recorded"], record["media"]] for record in records
        ]

        if albumNames:
            print(f"Albums by {artistName}:")

            for albumName in albumNames:
                (name, recorded, media) = albumName
                print(f"\t{name}: {recorded} ({media})")
        else:
            print(f"No albums found for {artistName}.")


def GetAllArtistsAndAlbums():
    artists = a.GetAllArtists()
    artistList = ad.CreateDictionaryList(artists)

    sortField = "recorded"
    records = r.GetAllRecords(sortField)
    recordList = rd.CreateDictionaryList(records)

    print("\nRecord List\n")

    for artist in artistList:
        print(f"{artist['name']}")

        for record in recordList:
            if record["artistid"] == artist["artistid"]:
                print(f"\t{record['recorded']}: {record['name']} ({record['media']})")

        print()


def GetRecordsByYear2(recordedYear: int):
    recordsByYear = r.GetRecordsByYear(recordedYear)

    artistRecordsDict = {}

    # Iterate through the records and group them by artist names
    for record in recordsByYear:
        artistid = record["artistid"]
        artistName = a.GetArtistName(artistid)

        if artistName not in artistRecordsDict:
            artistRecordsDict[artistName] = []

        artistRecordsDict[artistName].append(
            {"name": record["name"], "media": record["media"]}
        )

    print(f"\nArtists with albums recorded in {recordedYear}:\n")

    for artistName in artistRecordsDict:
        print(f"\n\t{artistName}:")
        artistRecords = artistRecordsDict[artistName]

        if artistRecords:
            for record in artistRecords:
                print(f"\t\t{record['name']} ({record['media']})")

    print()


def GetRecordsByYear(recordedYear: int):
    artists = a.GetAllArtists()

    sortField = "recorded"
    recordsByYear = r.GetRecordsByYear(recordedYear)
    recordList = rd.CreateDictionaryList(recordsByYear)
    count = len(recordList)

    if count == 0:
        print(f"No records found for {recordedYear}.")
        return

    artistIdsList = ad.GetArtistIds(recordList)

    artists = [artist for artist in artists if artist["artistid"] in artistIdsList]
    artistList = ad.CreateDictionaryList(artists)

    print("\nRecord List\n")

    for artist in artistList:
        print(f"{artist['name']}")

        for record in recordList:
            if record["artistid"] == artist["artistid"]:
                print(f"\t{record['recorded']}: {record['name']} ({record['media']})")

        print()


def GetAllRecords():
    sortField = "artistid"
    records = r.GetAllRecords(sortField)

    for record in records:
        stringDate = record["bought"]
        cost = record["cost"]

        print(
            f"{record['recordid']}: {record['artistid']}: - {record['name']} - \
{record['field']} - {record['recorded']} - {record['label']} - {record['pressing']} - \
{record['rating']} - {record['discs']} - {record['media']} - {stringDate} - {cost}."
        )


def CreateRecord(artistid: int):
    artist = a.GetMongoId(artistid)
    recordIdList = r.GetRecordIds()
    newRecordId = rd.GetNewRecordId(recordIdList)

    name = "Bong Drop"
    field = "Rock"
    recorded = 1995
    label = "Diddly Squat"
    pressing = "Aus"
    rating = "***"
    discs = 1
    media = "CD"
    bought = "2023-09-01 12:00:00"
    cost = 24.99

    document = {
        "artist": artist,
        "recordid": newRecordId,
        "artistid": artistid,
        "name": name,
        "field": field,
        "recorded": recorded,
        "label": label,
        "pressing": pressing,
        "rating": rating,
        "discs": discs,
        "media": media,
        "bought": bought,
        "cost": cost,
        "review": "A slightly disappointing effort for Alan.",
    }

    _id = r.AddNewRecord(document)

    print(_id)


def UpdateRecord(recordid: int):
    exists = r.CheckIfRecordExists(recordid)

    if exists:
        name = "Bongo Drop"
        pressing = "Australian"
        rating = "Slightly flawed"
        discs = 2
        media = "CD"
        bought = "01 Sept 2023"
        cost = "$24.99"
        review = "Pretty good album."

        query = {"recordid": recordid}
        newValues = {
            "$set": {
                "name": name,
                "pressing": pressing,
                "rating": rating,
                "discs": discs,
                "media": media,
                "bought": bought,
                "cost": cost,
                "review": review,
            }
        }

        affected = r.UpdateRecord(query, newValues)

        print(f"Number of documents updated: {affected}.")
    else:
        print(f"Record with Id: {recordid} not found!")


def GetRecordById(recordid):
    record = r.GetRecordById(recordid)

    if record:
        review = record["review"]
        abbreviatedReview = review if len(review) < 60 else review[:60] + "..."

        print(
            f"{record['recordid']}: {record['recorded']} - {record['name']} ({record['media']})\n\t{abbreviatedReview}"
        )


def DeleteRecord(recordid: int) -> int:
    query = {"recordid": recordid}

    affected = r.DeleteRecord(query)

    print(f"Number of documents deleted: {affected}.")


def GetRecordByName(name):
    query = {"name": {"$regex": f".*{name}.*", "$options": "i"}}

    records = r.GetRecordsByName(query)

    for record in records:
        print(
            f"Id: {record['recordid']} - {record['recorded']} - {record['name']} ({record['media']}) - Bought: {record['bought']} - Cost: {record['cost']}"
        )


def GetRecordsByArtistId(artistid: int):
    artist = a.GetArtistById(artistid)

    if artist:
        biography = artist["biography"]
        bio = biography if len(biography) < 60 else biography[:60] + "..."

        print(
            f"{artist['artistid']}: {artist['firstname']} - {artist['lastname']} - {artist['name']}\n\t{bio}"
        )
    else:
        print(f"No Artist with Id: {artistid} found!")
        return

    records = r.GetAllRecordsByArtist(artistid)

    if records:
        for record in records:
            review = record["review"]
            abbreviatedReview = review if len(review) < 60 else review[:60] + "..."

            print(
                f"(Id: {record['recordid']}): {record['recorded']} - {record['name']} ({record['media']}) - Bought: {record['bought']} - Cost: {record['cost']}\n\t{abbreviatedReview}"
            )


def GetTotalNumberOfCDs():
    total = r.GetTotalNumberOfCDs()

    print(f"Total number of CD discs: {total}.")


def GetTotalNumberOfCdDvds():
    total = r.GetTotalNumberOfCdDvds()

    print(f"Total number of CD/DVD disc sets: {total}.")


def GetTotalNumberOfCdBlurays():
    total = r.GetTotalNumberIfCdBlurays()

    print(f"Total number of CD/Blu-ray disc sets: {total}.")


def GetTotalNumberOfRecords():
    total = r.GetTotalNumberOfRecords()

    print(f"Total number of vinyl Records: {total}.")


def GetTotalNumberOfDVDs():
    total = r.GetTotalNumberOfDVDs()

    print(f"Total number of DVD's: {total}.")


def GetTotalNumberOfBlurays():
    total = r.GetTotalNumberOfBlurays()

    print(f"Total number of Blu-rays: {total}.")


def GetTotalNumberOfDiscs():
    total = r.GetTotalNumberOfDiscs()

    print(f"Total number of All discs: {total}.")


def GetArtistNumberOfRecords(artistid):
    artist = a.GetArtistById(artistid)
    total = r.GetArtistNumberOfRecords(artistid)

    print(f"Total number of {artist['name']} discs: {total}.")
