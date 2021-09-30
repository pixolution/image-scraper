# Want to scrape and download images for your own machine learning project?
## Use image scraper to download images that you want from the web!

Heavily inspired by fast.ai download_images

Run scrape-images.py to select what you want and download those images! Results sourced from [Duck Duck Go](https://duckduckgo.com/) search engine

Example on Command Prompt
```cmd
python scrape-images.py
What do you want:
fish
Number of images?
100
```

Gets you a folder with images in the following structure
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