# scraping-ebay

This project contains a set of scripts used to scrape Ebay's products data using Scrapy Web Crawling Framework.

In the current stage, the list of products scraped is defined by a search string (the same used in eBay web page). The search string can be changed in ebay.py file (located at scraping_ebay\spiders).

# How to use

You will need Python 3.x to run the scripts.
Python can be downloaded [here](https://www.python.org/downloads/).

You have to install ***scrapy*** framework:
* In command prompt/Terminal: *pip install scrapy*
* If you are using [Anaconda Python distribution](https://anaconda.org/anaconda/python): *conda install -c conda-forge scrapy*

Once you have installed *scrapy* framework, just clone/download this project, access the folder in command prompt/Terminal and run the following command:

*scrapy crawl ebay -o products.csv*

You can change the output format to JSON or XML by change the output file extension (ex: *products.json*).