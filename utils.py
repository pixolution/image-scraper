import requests
import re
import json
import os
from multiprocessing import Pool, cpu_count
from functools import partial
import imghdr
from pathlib import Path

def search_images_ddg(key,max_n=200):
    """Search for 'key' with DuckDuckGo and return a unique urls of 'max_n' images
       (Adopted from https://github.com/deepanprabhu/duckduckgo-images-api)
    """
    url        = 'https://duckduckgo.com/'
    params     = {'q':key}
    res        = requests.post(url,data=params)
    searchObj  = re.search(r'vqd=([\d-]+)\&',res.text)
    if not searchObj: print('Token Parsing Failed !'); return
    requestUrl = url + 'i.js'
    headers    = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0'}
    params     = (('l','us-en'),('o','json'),('q',key),('vqd',searchObj.group(1)),('f',',,,'),('p','1'),('v7exp','a'))
    urls       = []

    res  = requests.get(requestUrl,headers=headers,params=params)
    data = json.loads(res.text)
    while 'next' in data:
        for obj in data['results']:
            urls.append(obj['image'])
            max_n = max_n - 1
            if max_n <= 0 : return set(urls)

        requestUrl = url + data['next']

    return set(urls)

def download_image(dest, inp):
    """Downloads an image from a url to a destination
    """
    i, url = inp

    dest = Path(dest)
    dest.mkdir(exist_ok=True)

    try:
        file_path = url.split("?")[0]
        file_path = Path(file_path)

        suffix = file_path.suffix if file_path.suffix else '.jpg'

        name = i

        response = requests.get(url)
        path_name = f'{dest}/{name}{suffix}'

        with open(path_name, 'wb') as f:
            f.write(response.content)

    except Exception as e:
        print(e)
    
def download_in_parallel(dest, key, max_n):
    pool = Pool(cpu_count())
    urls = search_images_ddg(key=key, max_n=max_n)
    print(f'found {len(urls)} urls')
    download_func = partial(download_image, dest)
    results = pool.map(download_func, list(enumerate(urls)))
    pool.close()
    pool.join()

def remove_bad_images(folder):
    count = 0
    for filename in os.listdir(folder):
        path = f"{folder}/{filename}"
        if imghdr.what(path) is None:
            os.remove(path)
            count += 1
    print(f"Removed {count} images")


if __name__ == "__main__":
    download_in_parallel("fishimgs", "fish", 1)
    remove_bad_images('fishimgs')


