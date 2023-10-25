from pymongo import MongoClient, ASCENDING

"""
Search for albums by Year.
"""

client = MongoClient("mongodb://localhost:27017")

db = client["record-db"]

recorded_year = 1974

records_by_year = db["records"].find({"recorded": recorded_year})

artist_ids = list({record["artistid"] for record in records_by_year})

artists_in_year = db["artists"].find({"artistid": {"$in": artist_ids}})

artists_in_year = artists_in_year.sort(
    [("lastname", ASCENDING), ("firstname", ASCENDING)]
)

print(f"\nAlbums by year: {recorded_year}\n")

for artist in artists_in_year:
    print(f"\t{artist['name']}")

    # Create a new cursor for records by the year for each artist
    records_by_year = db["records"].find(
        {"recorded": recorded_year, "artistid": artist["artistid"]}
    )

    for record in records_by_year:
        print(f"\t\t{record['name']} ({record['media']})")

print()
