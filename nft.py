from PIL import Image
import json
import os
from random import randint
from random import seed

dirname = os.path.dirname(__file__)

#config items
project_name = "project name
base_uri = "https://ipfs.io/ipfs/"
total_nft = 2
rand_seed = 345698135


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


def generate_image(all_images):
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
        file = str(k) + ".png"
        rgb_im.save("./images/" + file)

        # save metadata
        token = {
            "image": base_uri + str(k) + '.png',
            "tokenId": k,
            "name": project_name + ' ' + str(k),
            "attributes": meta
        }

        with open('./metadata/' + str(k), 'w') as outfile:
            json.dump(token, outfile, indent=4)


def f(path):
    d = {}
    dirs = sorted(os.listdir(path))
    for i in dirs:
        if i != ".DS_Store":
            # skips .DS_Store
            sub_dir = os.path.join(path, i)
            files = os.listdir(sub_dir)
            names = [x.replace(".png", "") for x in files]
            if ".DS_Store" in names:
                skip = names.index(".DS_Store")
                names.pop(skip)
                d[i] = names
            else:
                d[i] = names
    return d


if __name__ == '__main__':
    attributes_mapping = f("./attributes")
    total_attributes = len(attributes_mapping)
    attributes = [i for i in attributes_mapping.keys()]

    print(attributes_mapping)
    # generate random images
    images = {}
    for x in range(0, total_nft):
        image = {}
        seed(x+rand_seed)
        # cycle through attributes
        temp = {}
        for i in attributes_mapping.keys():
            # get total options for attribute
            values = attributes_mapping[i]
            options = len(values)
            r = randint(options, options ** options)
            selection = (r // options)
            # adjust for index
            temp.update({i: values[selection-1]})
            seed(r)

        image[x] = temp
        images.update(image)

    # check uniqueness
    print("Duplicates Detected?", unique_check(images))

    # generate all images
    generate_image(images)

    # gather stats
    generate_mint_stats(images, attributes_mapping)
