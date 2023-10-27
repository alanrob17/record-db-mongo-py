from pymongo import MongoClient

"""
Search for albums by Year using a dictionary.
Same as recorded.py but uses dictionaries.
"""

client = MongoClient("mongodb://localhost:27017")

db = client["record-db"]

recorded_year = 1974
records_by_year = db["records"].find({"recorded": recorded_year})

artist_records_dict = {}

# Iterate through the records and group them by artist names
for record in records_by_year:
    artistid = record["artistid"]
    artist_name = db["artists"].find_one({"artistid": artistid})["name"]

    if artist_name not in artist_records_dict:
        artist_records_dict[artist_name] = []
    artist_records_dict[artist_name].append(
        {"name": record["name"], "media": record["media"]}
    )

print(f"\nArtists with albums recorded in {recorded_year}:\n")

for artist_name in artist_records_dict:
    print(f"\t{artist_name}:")
    artist_records = artist_records_dict[artist_name]

    if artist_records:
        for record in artist_records:
            print(f"\t\t{record['name']} ({record['media']})")
    else:
        print(f"No records for this artist in {recorded_year}")

print()
