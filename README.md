# Want to scrape and download images for your own machine learning project?
## Use image scraper to download images that you want from the web!

Heavily inspired by fast.ai download_images, forked from [theojl6/image-scraper/](https://github.com/theojl6/image-scraper/)

Run scrape-images.py to select what you want and download those images! Results sourced from [Duck Duck Go](https://duckduckgo.com/) search engine

## Install
* clone this repo
* create an virtual environment
```
cd image-scraper
python3 -mvenv venv
```
* enter virtual environment
```
source venv/bin/avtivate
```
* install requirements
```
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

## Usage

* search for images with a given keyword (e.g. fish)
```
python3 scrape-images.py
What do you want:
fish
Number of images?
100
```

* the resulting folder with images
```
image-scraper
├── fishimgs
│  ├── 0.jpg
│  ├── 1.jpg
│  ├── 2.jpg
│  └── ...
├── screenshots
├── .gitignore
├── image-scraper.py
├── utils.py
├── LICENSE
└── README.md
```

[MIT License](LICENSE)