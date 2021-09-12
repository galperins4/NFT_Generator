from PIL import Image
import json
import os
import pprint
from random import choices
from random import seed
import time
from utility.nftstorage import NftStorage
from utility.pinata import Pinata

dirname = os.path.dirname(__file__)

#config items
project_name = "project name"
base_uri = "https://ipfs.io/ipfs/"
total_nft = 2
rand_seed = 345698135
NFTSTORAGE = "Y"
NFTSTORAGE_API_KEY = "MyKey"
PINATA = "N"
PINATA_JWT = "MyJWT"


# rarity - customize for each layer / values
rarity = {"1-background": [0.25, 0.65, 0.10],
          "2-object": [0.10, 0.90],
          "3-text": [0.20, 0.30, 0.50]}


def unique_check(all_images):
    list_check = [tuple(v.items()) for k, v in all_images.items()]

    if len(list_check) == len(set(list_check)):
        return False
    else:
        return True


def generate_mint_stats(all_images, mapping):
    stats = {}

    keys = [i.split("-")[1] for i in mapping.keys()]
    values = [i for i in mapping.values()]

    for x in range(0, len(keys)):
        tmp = {}
        for y in range(0, len(values[x])):
            img_c = {values[x][y]: 0}
            tmp.update(img_c)
        stats[keys[x]] = tmp

    for k, v in all_images.items():
        img_key = [i.split("-")[1] for i in v.keys()]
        img_values = [i for i in v.values()]

        for x in range(0, len(img_key)):
            stats[img_key[x]][img_values[x]] += 1

    with open('./mint_stats', 'w') as outfile:
        json.dump(stats, outfile, indent=4)

    print("\nNft Image Statistics")
    pprint.pprint(stats)


def generate_image(all_images):
    nstorage = {}
    file_list = []
    meta_file_list = []
    # get images
    for k, v in all_images.items():
        meta = []
        directories = [i for i in v.keys()]
        imgnames = [i for i in v.values()]

        for x in range(0, len(directories)):
            att = {directories[x].split("-")[1]: imgnames[x]}
            meta.append(att)

        # if only 2 images to combine - single pass
        if len(v) <= 2:
            im1 = Image.open(f'./attributes/{directories[0]}/{imgnames[0]}.png').convert('RGBA')
            im2 = Image.open(f'./attributes/{directories[1]}/{imgnames[1]}.png').convert('RGBA')
            com = Image.alpha_composite(im1, im2)
        # if > 2 images to combine - multi pass
        else:
            im1 = Image.open(f'./attributes/{directories[0]}/{imgnames[0]}.png').convert('RGBA')
            im2 = Image.open(f'./attributes/{directories[1]}/{imgnames[1]}.png').convert('RGBA')
            com = Image.alpha_composite(im1, im2)
            counter = 2
            while counter < len(v):
                im = Image.open(f'./attributes/{directories[counter]}/{imgnames[counter]}.png').convert('RGBA')
                com = Image.alpha_composite(com, im)
                counter += 1

        # save image
        rgb_im = com.convert('RGB')
        file = "./images/"+ str(k) + ".png"
        file_list.append(file)
        rgb_im.save(file)  
        
        '''
        # If using NFT.Storage and flag is yes, upload file
        if NFTSTORAGE == 'Y':
            c = NftStorage(NFTSTORAGE_API_KEY)
            cid = c.upload(file)
            image = base_uri + cid
            nstorage[str(k)] = {"image_cid": cid}
            time.sleep(0.5)
        else:
            image = base_uri + str(k) + '.png'
        '''            
        # save metadata
        token = {
            "image": base_uri + str(k) + '.png',
            "tokenId": k,
            "name": project_name + ' ' + str(k),
            "attributes": meta
        }

        meta_file = './metadata/' + str(k)
        meta_file_list.append(meta_file)
        with open(meta_file, 'w') as outfile:
            json.dump(token, outfile, indent=4)
        '''          
        # If using NFT.Storage - also upload metadata
        if NFTSTORAGE == 'Y':
            c = NftStorage(NFTSTORAGE_API_KEY)
            cid = c.upload(meta_file)
            nstorage[str(k)].update({"metadata_cid": cid})
            time.sleep(0.5)
        '''
    '''
    # Check if using PINATA and pin to IPFS
    if PINATA == "Y":
         p = Pinata(PINATA_JWT)
         for k, v in nstorage.items():
              name = k + '.png'
              p.pin(name, v['image_cid'])
              meta = k + '.json'
              p.pin(meta, v['metadata_cid'])
    '''
    '''
    # write out NFT.Storage data
    with open('NFT_Storage_Information', 'w') as outfile:
         json.dump(nstorage, outfile, indent=4)
    ''' 
    print(meta_file_list)
    quit()
    if NFTSTORAGE == 'Y':
         c = NftStorage(NFTSTORAGE_API_KEY)
         # upload images 
         cid = c.upload(file_list, 'image/png')
         nstorage['image_directory_cid'] = cid

         # update Metadata with CID
         
         # upload 

    print(nstorage)
          

def update_meta_cid():
    pass
     
          
          
def confirm_trait_rarity(mapping):

    counter = 1
    for k,v in mapping.items():
        print("Layer {} Values:".format(counter), v)
        print("Trait Estimated Rarity:", rarity[k], "\n")
        counter +=1

    answer = ""
    while answer not in ["y", "n"]:
        answer = input("Are traits and rarity correct? [Y/N]? ").lower()
        if answer == "n":
            print("\nPlease update configuration and restart. Quiting NFT Generator")
            quit()

                    
def f(path):
    d = {}
    dirs = sorted([f for f in os.listdir(path) if not f.startswith('.')])
    for i in dirs:
        sub_dir = os.path.join(path, i)
        files = sorted([f for f in os.listdir(sub_dir) if not f.startswith('.')])
        d[i] = [s.replace(".png", "") for s in files]
    return d


if __name__ == '__main__':
    attributes_mapping = f("./attributes")
    total_attributes = len(attributes_mapping)
    confirm_trait_rarity(attributes_mapping)

    # generate random images
    images = {}
    for x in range(0, total_nft):
        image = {}
        seed(x+rand_seed)
        # cycle through attributes
        temp = {}
        for i in attributes_mapping.keys():
            # get values
            values = attributes_mapping[i]
            # get rarity weighting
            weights = rarity[i]
            selection = choices(values, weights)
            # add selection
            temp.update({i: selection[0]})

        image[x] = temp
        images.update(image)

    # check uniqueness
    print("Duplicates Detected?", unique_check(images))

    # generate all images
    generate_image(images)

    # gather stats
    generate_mint_stats(images, attributes_mapping)
