## Scrappy is an open source framework use to extract data from websites
## WebSpider: also refer as web crawler or web bot, is an automated program or script that systematically browses the World Wide Web to collect information. 
## They're usually employee by search engines to index web pages, but thet can also be used for various purposes such as data mining, web scrapping, and monitoring website changes. 

## Run pip install scrappy to install it. 
## We can use the scrappy command line interface: 
## $ scrapy startproject <name-of-the-project>

### Troubleshoot ###
## If errors like all_params = set(params) TypeError: unhashable type: 'list' appear, it seems like the Python version that you have can not handle the Scrappy packages. 
## Download 3.9.13
## Run a virtual env: $ python3.9 -m venv <name-of-virtual-environment-directory>
## Activate the virtual env: $ source virtual3/bin/<name-of-virtual-environment-directory>
## Check the version (it should print Python 3.9.13): $ python --version 
from pathlib import Path
import scrapy 

class SampleSpider(scrapy.Spider):
    name = "sample"
    start_urls = [
        'https://quotes.toscrape.com/page/1/',
        'https://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename,'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
