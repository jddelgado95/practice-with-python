## Web pages don't want their data to be scrapped. But a simple way to know what can and what can not be scrapped, use
## a robot file. You can find it if you add "/robots.txt" at the end of the URL. This is useful for spiders and web crawlers. 
## https://www.airbnb.co.cr/robots.txt
##User-agent: Googlebot
##Allow: /calendar/ical/
##Allow: /.well-known/amphtml/apikey.pub
##Disallow: /.well-known/assetlinks.json
##Disallow: /*/skeleton
##Disallow: /*/sw_skeleton
##Disallow: /alumni
##Disallow: /500
##Disallow: /account

## APIs helps us to get information from other web pages, apps, other programs.. etc. 

## Beautiful soup => library to scrap website, very old school by te way
## Install it: pip3 install beautifulsoup4

##request library: Requests allows to send HTTP/1.1 requests easily. There is no need to manually add query strings to URLs, or to form-encode PUT and POST data, just use the json method. 
## pip3 install requests

import requests ##Allowd us to donwload the HTML
from bs4 import BeautifulSoup ##allows to manipulate the HTMl and grab data

#create a respond
res = requests.get('https://news.ycombinator.com/news') ##gets the information
print(res) ##get a 200 respond which means that the status is OK. 
print(res.text) ##prints the entire HTML, we can use BeautifulSoup to clean the HTML. 

# we can use BeautifulSoup to convert the entire HTML into an object, so we can manipulate it easily. 
soup = BeautifulSoup(res.text,'html.parser') ## creates an object, in this case named soup, that converts the HTML string into something we can use. You can check the documentation of BeautifulSoup in order to check which other formats BeautifulSoup can parse. 

#print(soup) ## if you check this you can now see that the entire HTML has a format. 
#print(soup.body) ##prints just the body
#print(soup.content) ##prints just the content
#print(soup.find_all('div')) #prints onlty the div objects inb a list form. 
#print(soup.find_all('a')) #prints all the links
#print(soup.title) #prints only tge title. 
#print(soup.a) #prints the first 'a' tag that comes up
#print(soup.find('a')) #prints the first 'a' tag
#print(soup.find(id='43675126')) #find a specific element based on its ID. 
#print(soup.select('#score_43673551')) #find a specific css element or class based on its ID, uses css selectors.



