import artist_test as at
import record_test as rt

# -- Artist Methods --

# at.GetAllArtists()

# at.CreateArtist()

# artistid = 823
# at.UpdateArtist(artistid)

# artistid = 823
# at.DeleteArtist(artistid)

# name = "Bob Dylan"
# at.GetArtistByName(name)

# artistid = 114
# at.GetArtistById(artistid)

# artistid = 114
# at.GetBiography(artistid)

# artistid = 114
# at.ArtistHtml(artistid)

# firstName = "Bob"
# lastName = "Dylan"
# at.GetArtistId(firstName, lastName)

# at.GetArtistsWithNoBio()

# at.GetNoBiographyCount()

# name = "allman"
# at.GetArtistByPartialName(name)


# -- Record Methods --

# rt.GetAllArtistsAndAlbums()

# artist = "Bob Dylan"
# rt.GetArtistAndAlbums(artist)

# year = 1974
# rt.GetRecordsByYear(year)

# year = 1974
# rt.GetRecordsByYear2(year)

# rt.GetAllRecords()

# artistid = 823
# rt.CreateRecord(artistid)

# recordid = 5251
# rt.UpdateRecord(recordid)

# recordid = 5251
# rt.DeleteRecord(recordid)

# recordid = 5250
# rt.GetRecordById(recordid)

# name = "blonde"
# rt.GetRecordByName(name)

# artistid = 114
# rt.GetRecordsByArtistId(artistid)

# rt.GetTotalNumberOfCDs()

# rt.GetTotalNumberOfCdDvds()

# rt.GetTotalNumberOfCdBlurays()

# rt.GetTotalNumberOfRecords()

# rt.GetTotalNumberOfDVDs()

# rt.GetTotalNumberOfBlurays()

# rt.GetTotalNumberOfDiscs()

# artistid = 114
# rt.GetArtistNumberOfRecords(artistid)

# rt.GetRecordList()

## I have built this previously but in this version
## I need to be able to join two tables together in a query.
## Work on how to do this in Python.
# recordid = 2196
# rt.GetArtistRecordEntities(recordid)

# recordid = 2196
# rt.GetRecordDetails(recordid)

# recordid = 2196
# rt.GetArtistNameFromRecord(recordid)

# year = 1971
# rt.GetDiscCountForYear(year)

## This run to update Cost and Bought fields
## *** Don't run again! ***
# rt.UpdateCostAndBoughtDates()

# year = 2000
# rt.GetBoughtDiscCountForYear(year)

# rt.GetNoRecordReview()

# rt.GetNoReviewCount()

# artistid = 114
# rt.GetTotalArtistCostById(artistid)

rt.GetTotalArtistCost()

# recordid = 2196
# rt.RecordHtml(recordid)
