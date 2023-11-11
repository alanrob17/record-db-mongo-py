import artist_db as a
import artist_data as ad


def GetAllArtists():
    artists = a.GetAllArtists()

    for artist in artists:
        biography = artist["biography"]
        abbreviatedBio = biography if len(biography) < 60 else biography[:60] + "..."

        print(f"{artist['artistid']}: {artist['name']} - {abbreviatedBio}")


def CreateArtist():
    artistIdList = a.GetArtistIds()
    newArtistId = ad.GetNewArtistId(artistIdList)

    firstName = "Alan"
    lastName = "Robson"
    name = lastName if not firstName else f"{firstName} {lastName}"
    biography = "Bob is a Country & Western singer."

    exists = a.CheckIfArtistExists(name)

    if exists:
        print(f"Artist {name} already exists!")
        return

    document = {
        "artistid": newArtistId,
        "firstname": firstName,
        "lastname": lastName,
        "name": name,
        "biography": biography,
    }

    _id = a.AddNewArtist(document)

    print(_id)


def UpdateArtist(artistid: int):
    exists = a.CheckIfArtistIdExists(artistid)

    if exists:
        artistid = artistid
        firstName = "Alan"
        lastName = "Robson"
        name = lastName if not firstName else f"{firstName} {lastName}"
        biography = "Alan is a Soul & Torch singer."

        query = {"artistid": artistid}
        newValues = {
            "$set": {
                "firstname": firstName,
                "lastname": lastName,
                "name": name,
                "biography": biography,
            }
        }

        affected = a.UpdateArtist(query, newValues)

        print(f"Number of documents updated: {affected}.")
    else:
        print(f"Artist with Id: {artistid} doesn't exist!")


def DeleteArtist(artistid: int) -> int:
    query = {"artistid": artistid}

    affected = a.DeleteArtist(query)

    print(f"Number of documents deleted: {affected}.")


def GetArtistByName(name: str):
    artist = a.GetArtistByName(name)

    if artist:
        print(f"{artist['artistid']}: {artist['firstname']} {artist['lastname']}")


def GetArtistById(artistid: int):
    artist = a.GetArtistById(artistid)

    if artist:
        biography = artist["biography"]
        bio = biography if len(biography) < 60 else biography[:60] + "..."

        print(
            f"{artist['artistid']}: {artist['firstname']} - {artist['lastname']} - {artist['name']}\n\t{bio}"
        )


def GetBiography(artistid: int):
    biography = a.GetBiography(artistid)

    if biography:
        print(biography)


def ArtistHtml(artistid: int):
    artist = a.GetArtistById(artistid)

    if artist:
        biography = artist["biography"]
        bio = biography if len(biography) < 60 else biography[:60] + "..."
        htmlCode = f"<p><strong>Id:</strong> {artist['artistid']}</p>\n<p><strong>Name:</strong> {artist['firstname']} {artist['lastname']}</p>\n<p><strong>Biography:</strong></p>\n<div>{artist['biography']}</p></div>"

        print(htmlCode)


def GetArtistId(firstName: str, lastName: str):
    artistid = a.GetArtistIdByNames(firstName, lastName)

    if artistid:
        print(f"{artistid}: {firstName} {lastName}")


def GetArtistsWithNoBio():
    artists = a.GetArtistsWithNoBio()

    for artist in artists:
        print(f"Id: {artist['artistid']}, Name: {artist['name']}")


def GetNoBiographyCount():
    count = a.GetNoBiographyCount()

    if count:
        print(f"The number of Artists that have no Biography: {count}")


def GetArtistByPartialName(name):
    query = {"name": {"$regex": f".*{name}.*", "$options": "i"}}

    artists = a.GetArtistByPartialName(query)

    for artist in artists:
        biography = artist["biography"]
        abbreviatedBio = biography if len(biography) < 60 else biography[:60] + "..."

        print(
            f"Id: {artist['artistid']} - {artist['firstname']} - {artist['lastname']} - {artist['name']})\n\t{abbreviatedBio}"
        )
