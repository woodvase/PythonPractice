"""
[
        {
            "firstName": "Lynsey",
            "lastName": "Forsmark",
            "email": "lforsmark@hubspotpartners.com",
            "country": "United States",
            "availableDates": [
                "2017-04-14",
                "2017-04-19",
                "2017-04-21",
                "2017-04-22",
                "2017-04-23",
                "2017-04-24",
                "2017-05-07"
            ]
        },
        {
            "firstName": "Young",
            "lastName": "Mallone",
            "email": "ymallone@hubspotpartners.com",
            "country": "United States",
            "availableDates": [
                "2017-04-17",
                "2017-04-20",
                "2017-04-22",
                "2017-04-23",
                "2017-04-24",
                "2017-04-26",
                "2017-04-29",
                "2017-05-02"
            ]
        }
]
"""

from collections import defaultdict
from datetime import date, timedelta
from itertools import groupby


class DataFilter:
    def constructMapFromValidData(self, partners):
        mappedData = dict()
        for country, guests in groupby(partners, key=lambda x: x["country"]):
            mappedData[country] = defaultdict(list)
            for guest in guests:
                availableDates = [date.fromisoformat(dstr) for dstr in guest["availableDates"]]
                sortedDates = sorted(availableDates)
                for i, d in enumerate(sortedDates):
                    if i > 0 and sortedDates[i - 1] == d - timedelta(days=1):
                        startDate = sortedDates[i - 1]
                        mappedData[country][startDate].append(guest["email"])
        return mappedData

    """
    {
        country: {
            date1: [emails]
            date2: [emails]
            ...
            date3: [emails]
        }
    }
    """

    def filterFromMap(self, mappedData):
        result = {"countries": []}

        for key, value in mappedData.items():
            sortedDates = sorted(value.items(), key=lambda kv: (-len(kv[1]), kv[0]))
            entry = dict()
            entry["name"] = key
            if len(sortedDates):
                startDate = sortedDates[0]
                entry["attendeeCount"] = len(startDate[1])
                entry["attendees"] = sorted(startDate[1])
                entry["startDate"] = startDate[0].isoformat()
            else:
                entry["attendeeCount"] = 0
                entry["attendees"] = []
                entry["startDate"] = None
            result["countries"].append(entry)

        return result
