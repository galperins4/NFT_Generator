import requests

class NftStorage:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = 'https://api.nft.storage/upload'
        self.headers = {'Authorization': 'Bearer ' + self.api_key}
        
    
    def upload(self, file_list, file_type):
        files = []
        for i in file_list:
            files.append(('file', (i, open(i, 'rb'), file_type)))
        
        try:
            response = requests.post(self.url, headers = self.headers, files = files)
            if r.json()['ok'] == True:
                return r.json()['value']['cid']
        except:
            print("Something went wrong with the upload")
            
    '''
    def upload(self, file):
        data = open(file, 'rb').read()
        try:
            response = requests.post(self.url, headers = self.headers, data = data)
            if response.json()['ok'] == True:
                return response.json()['value']['cid']
        except:
            print("Something went wrong with the upload")
     '''
