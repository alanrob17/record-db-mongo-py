def GetNewArtistId(artistIdList: list) -> int:
    artistIdList.sort(reverse=True)
    artistid = artistIdList[0]
    artistid += 1

    return artistid


## ArtistList in memory - you wouldn't use this for a huge list of documents.
def CreateDictionaryList(artists: list[dict]) -> list[dict]:
    artistList = []
    for artist in artists:
        artistList.append(artist)

    return artistList


def GetArtistIds(records):
    # Create a set to store distinct artist_ids
    artistIds = set()

    for record in records:
        artistIds.add(record["artistid"])

    # Convert the set to a list if needed
    artistIdsList = list(artistIds)

    return artistIdsList
