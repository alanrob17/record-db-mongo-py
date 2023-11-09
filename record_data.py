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
