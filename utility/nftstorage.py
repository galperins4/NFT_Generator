import requests

class NftStorage:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = 'https://api.nft.storage/upload'
        self.headers = {'Authorization': 'Bearer ' + self.api_key}
        
    
    def upload(self, file):
        data = open(file, 'rb').read()
        try:
            response = requests.post(self.url, headers = self.headers, data = data)
            if response.json()['ok'] == True:
                return response.json()['value']['cid']
        except:
            print("Something went wrong with the upload")
