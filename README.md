# RecordDB using MongoDB and Python

I am currently teaching myself Python and started developing routines using MongoDB on a version of my Record DB.

My database name is **RecordDB** and I have two related collections of data named ``artists`` and ``records``.

This an example of the ``artists`` JSON.

 ```json
    {
     "_id": "6324401d9926786e6c05479e",
     "artistid": 114,
     "firstname": "Bob",
     "lastname": "Dylan",
     "name": "Bob Dylan",
     "biography": "<p>Bob Dylan's influence...</p>",
     "__v": 0
    }
 ```

This is an example of the ``records`` JSON.

```json
 {
  "artist": "6324401d9926786e6c05479e",
  "recordid": 1172,
  "artistid": 114,
  "name": "Blonde On Blonde",
  "field": "Rock",
  "recorded": 1966,
  "label": "Columbia",
  "pressing": "American",
  "rating": "Indispensible",
  "discs": 1,
  "media": "CD-Audio",
  "bought": "17 Feb 1999",
  "cost": "$14.00",
  "review": "<p>If Highway 61 Revisited...</p>"
 }
```

These collections are related on ``artists.artistid`` = ``records.artistid``. I know this is redundent and that I could have joined these on the ``artist`` field in each collection.

I also could have joined the two collections together into one collection but I am keeping the data in a similar format to the SQL Server version of the database.

I am building a number of routines using Python to consume data for the database.

## dependencies

```bash
    pip install pymongo
```
