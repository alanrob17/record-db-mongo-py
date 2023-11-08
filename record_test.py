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


# def GetRecordsByYear(recordedYear: int):
#     recordsByYear = r.GetRecordsByYear(recordedYear)

#     artistRecordsDict = {}

#     # Iterate through the records and group them by artist names
#     for record in recordsByYear:
#         artistid = record["artistid"]
#         artistName = a.GetArtistName(artistid)

#         if artistName not in artistRecordsDict:
#             artistRecordsDict[artistName] = []

#         artistRecordsDict[artistName].append(
#             {"name": record["name"], "media": record["media"]}
#         )

#     print(f"\nArtists with albums recorded in {recordedYear}:\n")

#     for artistName in artistRecordsDict:
#         print(f"\n\t{artistName}:")
#         artistRecords = artistRecordsDict[artistName]

#         if artistRecords:
#             for record in artistRecords:
#                 print(f"\t\t{record['name']} ({record['media']})")

#     print()


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
