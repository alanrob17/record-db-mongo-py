def GetNewArtistId(artistIdList: list) -> int:
    artistIdList.sort(reverse=True)
    artistid = artistIdList[0]
    artistid += 1

    return artistid


def CreateDictionaryList(artists: list[dict[str, str]]) -> list[dict[str, str]]:
    artistList = [
        {
            "artistid": artist["artistid"],
            "firstname": artist["firstname"],
            "lastname": artist["lastname"],
            "name": artist["name"],
            "biography": artist["biography"],
        }
        for artist in artists
    ]

    return artistList


def GetArtistIds(records):
    # Create a set to store distinct artist_ids
    artist_ids = set()

    for record in records:
        artist_ids.add(record["artistid"])

    # Convert the set to a list if needed
    artist_ids_list = list(artist_ids)

    return artist_ids_list
