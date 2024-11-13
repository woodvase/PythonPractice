import json
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from itertools import groupby


class CallsFilter:
    def countMaxOverlappingCalls(self, callRecords):
        callsForAllDays = self.createCallsForEachDay(callRecords)
        mappedData = dict()
        grouped = self.groupByCustomerId(callsForAllDays)
        for customerId, calls in grouped:
            mappedData[customerId] = dict()
            callsByDate = self.groupByDate(calls)
            for date, callsInDay in callsByDate:
                r = self.countMaxOverlappingCallsForDay(callsInDay)
                mappedData[customerId][date] = {
                    "customerId": customerId,
                    "date": date,
                    "maxConcurrentCalls": r[0],
                    "timestamp": r[2],
                    "callIds": r[1],
                }

        return self.formatMappedData(mappedData)

    def countMaxOverlappingCallsForDay(self, callRecords):
        toBeSorted = []
        for call in callRecords:
            toBeSorted.append((call["startTimestamp"], "startTimestamp", call))
            toBeSorted.append((call["endTimestamp"], "endTimestamp", call))
            sortedCalls = sorted(toBeSorted, key=lambda x: (x[0], x[1]))

        callIds = []
        timestamp = 0
        maxCount = 0
        cnt = 0
        callIdsSet = set()
        for e in sortedCalls:
            if e[1] == "startTimestamp":
                cnt += 1
                if cnt > maxCount:
                    maxCount = cnt
                    callIdsSet.add(e[2]["callId"])
                    callIds = list(callIdsSet)
                    timestamp = e[2]["startTimestamp"]
            elif e[1] == "endTimestamp":
                cnt -= 1
                callIdsSet.discard(e[2]["callId"])
        return (maxCount, callIds, timestamp)

    def createCallsForEachDay(self, callRecords):
        result = []
        for call in callRecords:
            callStartTimestamp = call["startTimestamp"]
            call_start_date = self.getDateFromEpoch(callStartTimestamp)
            callEndTimestamp = call["endTimestamp"]
            call_end_date = self.getDateFromEpoch(callEndTimestamp)
            if call_end_date > call_start_date:
                while call_start_date < call_end_date:
                    newStartTimestamp = callStartTimestamp
                    newEndDatetime = datetime(
                        call_start_date.year,
                        call_start_date.month,
                        call_start_date.day,
                        tzinfo=timezone.utc,
                    ) + timedelta(days=1, seconds=-1)
                    newEntry = {
                        "customerId": call["customerId"],
                        "callId": call["callId"],
                        "startTimestamp": newStartTimestamp,
                        "endTimestamp": int(newEndDatetime.timestamp() * 1000),
                    }
                    result.append(newEntry)
                    call_start_date = (newEndDatetime + timedelta(seconds=1)).date()
                    callStartTimestamp = (
                        datetime(
                            call_start_date.year,
                            call_start_date.month,
                            call_start_date.day,
                            tzinfo=timezone.utc,
                        ).timestamp()
                        * 1000
                    )

                if callStartTimestamp < callEndTimestamp:
                    lastNewEntry = {
                        "customerId": call["customerId"],
                        "callId": call["callId"],
                        "startTimestamp": callStartTimestamp,
                        "endTimestamp": callEndTimestamp,
                    }
                    result.append(lastNewEntry)
            else:
                result.append(call)
        return result

    def getDateFromEpoch(self, unixTime: float) -> date:
        dt = datetime.fromtimestamp(unixTime / 1000, timezone.utc)
        return dt.date()

    """
    customerId:
        date: {
            timesStamp:
            callIds:
        }
    """

    def formatMappedData(self, mappedData):
        result = {"results": []}

        for _, daysData in mappedData.items():
            for _, info in daysData.items():
                result["results"].append(info)
        return result

    def groupByCustomerId(self, callRecords):
        r = defaultdict(list)
        for call in callRecords:
            r[call["customerId"]].append(call)
        return r.items()

    def groupByDate(self, callRecords):
        r = defaultdict(list)
        for call in callRecords:
            callStartTimestamp = call["startTimestamp"]
            call_start_date = self.getDateFromEpoch(callStartTimestamp)
            r[call_start_date.isoformat()].append(call)
        return r.items()
