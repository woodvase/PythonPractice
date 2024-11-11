import json

from callsFilter import CallsFilter
from data import DataAccess

"""
Find the max concurrent calls for customers per day
calls can be expanded to multi days
If there is no calls for the day, don't return result
calls end datetime is bigger then the start datetime
example data:

{
    "callRecords": [
        {
            "customerId": 123,
            "callId": "Jan1st_11:30pm_to_Jan1st_11:40pm_Call",
            "startTimestamp": 1704151800000,
            "endTimestamp": 1704152400000
        },
        {
            "customerId": 123,
            "callId": "Jan2nd_11:50pm_to_Jan3rd_12:20am_Call",
            "startTimestamp": 1704239400000,
            "endTimestamp": 1704241200000
        },
        {
            "customerId": 123,
            "callId": "Jan3rd_12:10am_to_Jan3rd_1:00am_Call",
            "startTimestamp": 1704240600000,
            "endTimestamp": 1704243600000
        },
        {
            "customerId": 123,
            "callId": "Jan4th_11:00pm_to_Jan5th_12:00am_Call",
            "startTimestamp": 1704409200000,
            "endTimestamp": 1704412800000
        }
    ]
}
"""


class Solution:
    def test(self, debug=False):
        da = DataAccess()
        input = da.GetData()
        r = input["callRecords"]
        callsFilter = CallsFilter()
        ans = callsFilter.countMaxOverlappingCalls(r)
        print(json.dumps(ans["results"], indent=4))
        resonse = da.PostData(ans)
        return resonse


s = Solution()
print(s.test())
