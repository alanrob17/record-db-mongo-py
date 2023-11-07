def GetNewArtistId(artistIdList: list) -> int:
    artistIdList.sort(reverse=True)
    artistid = artistIdList[0]
    artistid += 1

    return artistid
