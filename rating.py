import pymongo

"""
Search for all ratings in the records collection
"""

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["record-db"]

my_rating = "Indispensible"

records_by_rating = db["records"].find({"rating": my_rating})

artist_ids = list({record["artistid"] for record in records_by_rating})

artists_in_rating = db["artists"].find({"artistid": {"$in": artist_ids}})

artists_in_rating = artists_in_rating.sort(
    [("lastname", pymongo.ASCENDING), ("firstname", pymongo.ASCENDING)]
)

print(f"\nAlbums by rating: {my_rating}\n")

for artist in artists_in_rating:
    print(f"\n\t{artist['name']}")

    # Create a new cursor for records by the year for each artist
    records_by_rating = db["records"].find(
        {"rating": my_rating, "artistid": artist["artistid"]}
    )

    records_by_rating = records_by_rating.sort([("recorded", pymongo.ASCENDING)])

    for record in records_by_rating:
        print(f"\t\t{record['recorded']} - {record['name']} ({record['media']})")

print()
