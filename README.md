# NFT Generator
Python NFT Generator

## Prerequisites

1. Clone Repository
```git clone https://github.com/galperins4/NFT_Generator```

2. Install Pillow Dependency
``` pip3 install pillow ```

## Configuration and Usage

1. Update config items in nft.py (under import statements)

| Config Option | Default Setting | Description | 
| :--- | :---: | :--- |
| project_name | project name | Name of Project |
| base_uri | https://ipfs.io/ipfs/ | URI link for where NFT is hosted (e.g., IPFS) |
| total_nft| 2 | How many NFT's you want to mint |
| rand_seed| 345698135 | Random value for pseudo-random number generator |
| NFTSTORAGE| N | Y/N Option - Enables upload of images and metadata jsons to [nft.storage](https://nft.storage) |
| NFTSTORAGE_API_KEY| MyKey | [nft.storage](https://nft.storage) API Key |
| PINATA| N | Y/N Option - Enables pinning of images and metadata jsons to [pinata](https://app.pinata.cloud/) |
| PINATA_JWT| MyJWT | [pinata](https://app.pinata.cloud/) JWT Token |

2. Update estimated rarity in the section under the config items (See example below). Adjust the folder names to match your project and assign rarity to each layers attrbutes. Rarity order should be based on alphabetical file order in layer folder. These values should sum to 1 for each layer.

```rarity = {"1-background": [0.25, 0.65, 0.10], "2-object": [0.10, 0.90], "3-text": [0.20, 0.30, 0.50]}```

3. Load .png image files into the attributes folders. An few examples have been provided to test the script. The nomenclature of the folders is as follows: layer-attribute. So for example 1-background is the first layer used which contains background images. 

Important: All image files should be the same size (e.g., 400 x 400 pixels)

4. Run the script
``` python3 nft.py```

The script will do the following:
 - Display a confirmation screen [Y/N] that the attributes/rarity are correct per layer
 - Generate Images
 - Run a duplicate check (Note: this could occur with a low number of attributes/traits)
 - Output NFT images in to the ./images folder
 - Output Metadata for images in the ./metadata folder
 - Output a mint stats.json file with the full collection statistics (e.g., how many of each attribute/trait was selected)

Note: If using [nft.storage](https://nft.storage) functionality - considering running the script disabled first to confirm images. Once everything looks ok, re-rerun the script with the option enabled to upload all images and associated metadata to [nft.storage](https://nft.storage)

## Credits
Inspiration for this script was drawn from the public repositories of the creators of BitBirds and Weird Whales. Their main profiles are linked below:

[nft-fun](https://github.com/nft-fun)

[benyaminahmed](https://github.com/benyaminahmed)

## Changelog

### 0.4 
 - Added [pinata](https://app.pinata.cloud/) functionality

### 0.3
 - Added [nft.storage](https://nft.storage) functionality

### 0.2
 - Added rarity feature

### 0.1
 - Initial Release

## License
[MIT](LICENSE) © [galperins4](https://github.com/galperins4)
