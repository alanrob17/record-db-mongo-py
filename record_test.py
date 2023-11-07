# from pymongo import MongoClient as MC, ASCENDING
# from config import MONGODB_CONNECTION_STRING, DATABASE_NAME
import artist_db as ad

# import artist_test as at
import record_db as rd


def searchAllArtistsAndAlbums():
    """
    TODO: Refactor this code. At present it is making
        a database call to records for each artist
        in artists and is inefficient.
    """

    artists = ad.GetAllArtists()

    print(f"\nAlbums")

    for artist in artists:
        print(f"\n\t{artist['name']}")

        records = rd.GetAllRecordsByArtist(artist["artistid"])

        for record in records:
            print(f"\t\t{record['recorded']} - {record['name']} ({record['media']})")

    print()


def GetArtistAndAlbums(artistName: str):
    artist = ad.GetArtistByName(artistName)

    if artist:
        artistid = artist["artistid"]
    else:
        print(f"Artist '{artistName}' not found in the 'artists' collection.")
        artistid = None

    if artistid is not None:
        records = rd.GetArtistRecords(artistid)

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
