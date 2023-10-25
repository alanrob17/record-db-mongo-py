import pymongo

"""
Search for all Artists and their Albums.
"""

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["record-db"]

all_artists = db["artists"].find()

all_artists = all_artists.sort(
    [("lastname", pymongo.ASCENDING), ("firstname", pymongo.ASCENDING)]
)

print(f"\nAlbums")

for artist in all_artists:
    print(f"\n\t{artist['name']}")

    # Create a new cursor for records by the year for each artist
    all_records_by_artist = db["records"].find({"artistid": artist["artistid"]})

    all_records_by_artist = all_records_by_artist.sort(
        [("recorded", pymongo.ASCENDING)]
    )

    for record in all_records_by_artist:
        print(f"\t\t{record['recorded']} - {record['name']} ({record['media']})")

print()
