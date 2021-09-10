import requests
import time

class Pinata:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = 'https://api.pinata.cloud/pinning/pinByHash'
        self.headers = {'Authorization': 'Bearer ' + self.api_key}
        
        
    def pin(self, name, cid):
        metadata = {"name": name}
        payload = {"pinataMetadata": metadata, "hashToPin": cid}
        
        try:
            response = requests.post(self.url, headers = self.headers, json = payload)
            time.sleep(1)
        except:
            print("Something went wrong with the Pinata Pin")
