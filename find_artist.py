from pymongo import MongoClient, DESCENDING

"""
Search for an Artist and their Albums.
"""

client = MongoClient("mongodb://localhost:27017")

db = client["record-db"]

artist_name = "Bob Dylan"

artist_document = db["artists"].find_one({"name": artist_name})

if artist_document:
    artistid = artist_document["artistid"]
else:
    print(f"Artist '{artist_name}' not found in the 'artists' collection.")
    artistid = None

if artistid is not None:
    records = (
        db["records"].find({"artistid": artistid}).sort([("recorded", DESCENDING)])
    )

    album_names = [
        [record["name"], record["recorded"], record["media"]] for record in records
    ]

    if album_names:
        print(f"Albums by {artist_name}:")

        for album_name in album_names:
            print(f"\t{album_name[1]}: {album_name[0]} ({album_name[2]})")
    else:
        print(f"No albums found for {artist_name}.")
