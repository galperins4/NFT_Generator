# NFT Generator
Python NFT Generator

## Prerequisites

1. Clone Repository
```git clone https://github.com/galperins4/NFT_Generator```

2. Install Pillow Dependency
``` pip3 install pillow ```

## Configuration and Usage

1. Update config items in main.py (under import statements)

| Config Option | Default Setting | Description | 
| :--- | :---: | :--- |
| project_name | 0 | Name of Project |
| base_uri | https://ipfs.io/ipfs/ | URI link for where NFT is hosted (e.g., IPFS) |
| total_nft| 2 | How many NFT's you want to mint |
| rand_seed| 345698135 | Random value for pseudo-random number generator |

2. Load .png image files into the attribute folders. An example has been provided to test. The nomenclature is layer-attribute. So for example 1-background is the first layer used which contains background images. 

Important: All image files should be the same size (e.g., 400 x 400 pixels)

3. Run the script
``` python3 main.py```

The script will do the following:
 - Generate Images
 - Run a duplicate check (Note: this could occur with a low number of attributes/traits)
 - Output NFT images in to the ./images folder
 - Output Metadata for images in the ./metadata folder
 - Output a mint stats.json file with the full collection statistics (e.g., how many of each attribute/trait was selected)

## Credits
Inspiration for this script was drawn from the public repositories of the creators of BitBirds and Weird Whales. Their main profiles are linked below:
[nft-fun](https://github.com/nft-fun)
[benyaminahmed](https://github.com/benyaminahmed)

## Changelog

### 0.1
 - Initial Release

## License
[MIT](LICENSE) © [galperins4](https://github.com/galperins4)
