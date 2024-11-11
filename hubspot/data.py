import requests
from constant import URLs


class DataAccess:
    def __init__(self):
        return

    def GetData(self):
        try:
            url = URLs["GET_ENDPOINT"]
            response = requests.get(url)
            return response.json()
        except:
            print("Error when GetData")

    def PostData(self, payload):
        try:
            response = requests.post(URLs["POST_ENDPOINT"], json=payload)
            return response.json()
        except:
            print("Error when PostData")
