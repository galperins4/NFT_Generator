import requests

class NftStorage:
    def __init__(self, api_key):
        #self.image = image
        #self.metadata = metadata
        self.api_key = api_key
        self.url = 'https://api.nft.storage/upload'
        self.headers = {'Authorization': 'Bearer ' + self.api_key}
        
        #image_cid = self.upload_image()
        #metadata_cid = self.upload_metadata(image_cid)
        
        #output = {"image_cid": image_cid, "metadata_cid": metadata_cid}
        #return output
        
    
    def upload(self, file):
        data = open(file, 'rb').read()
        try:
            response = requests.post(self.url, headers = self.headers, data = data)
            if response.json()['ok'] == True:
                return response.json()['value']['cid']
        except:
            print("Something went wrong with the upload")
      
    '''  
    def upload_metadata(self, image_cid):
        data = open(self.metadata, 'rb').read()
        try:
            response = requests.post(self.url, headers = self.headers, data = data)
            if response.json()['ok'] == True:
                return response.json()['value']['cid']
         except:
            print("Something went wrong with the upload")
            quit()
    '''
