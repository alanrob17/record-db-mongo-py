from datetime import datetime


## RecordList in memory - you wouldn't use this for a huge list of documents.
def CreateDictionaryList(records: list[dict]) -> list[dict]:
    recordList = []
    for record in records:
        recordList.append(record)

    return recordList


def GetNewRecordId(recordIdList: list) -> int:
    recordIdList.sort(reverse=True)
    recordid = recordIdList[0]
    recordid += 1

    return recordid


def ChangeDate(stringDate):
    month_mapping = {
        "Jan": "01",
        "Feb": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "Aug": "08",
        "Sept": "09",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12",
    }

    if stringDate == "Unknown" or stringDate == "":
        date = "1900-01-01 12:00:00.000000"
    else:
        (day, month, year) = stringDate.split(" ")
        month = month_mapping.get(
            month, month
        )  # Use the mapping or keep original if not found

        date = f"{year}-{month}-{day} 12:00:00.000000"

    return date


def formatDateString(stringDate: str) -> str:
    stringDateTime = stringDate.split(" ")
    stringDate = stringDateTime[0]
    dateFormat = "%Y-%m-%d"
    date = datetime.strptime(stringDate, dateFormat)
    year = date.strftime("%Y")
    fmtDate = date.strftime("%d %b %Y")

    if year == "1900":
        fmtDate = "unk"

    return fmtDate
