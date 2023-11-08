def CreateDictionaryList(records: list[dict[str, str]]) -> list[dict[str, str]]:
    recordList = [
        {
            "recordid": record["recordid"],
            "artistid": record["artistid"],
            "name": record["name"],
            "field": record["field"],
            "recorded": record["recorded"],
            "label": record["label"],
            "pressing": record["pressing"],
            "rating": record["rating"],
            "discs": record["discs"],
            "media": record["media"],
            "bought": record["bought"],
            "cost": record["cost"],
        }
        for record in records
    ]

    return recordList
