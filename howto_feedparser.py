## Universal Feed Parser is a Python module for downloading and parsing syndicated feeds. It can handle RSS 0.90, Netscape RSS 0.91, Userland RSS 0.91, RSS 0.92, RSS 0.93, RSS 0.94, RSS 1.0, RSS 2.0, Atom 0.3, Atom 1.0, CDF and JSON feeds.

import feedparser
import newspaper 

bbc = feedparser.parse('https://feeds.bbci.co.uk/news/rss.xml')
print(bbc.feed) # prints all the information
print(bbc.feed.title) #prints the title
print(bbc.feed.description) #prints the description
print(bbc.feed.updated) #prints the newest update

#print the entries
print(bbc.entries) ## knows the length of the entries
print(bbc.entries[0])## prints first element of the entries
print(bbc.entries[0].title) ## prints the title of the first element
print(bbc.entries[0].link)## prints the link of the first element

article = newspaper.Article(bbc.entries[0].link)
article.download()
print(article.html)
article.parse()
print(article.title) #prints the name of the article
print(article.text) #prints the full text of the article

# deal with missing items
bbc.feed.get('missing','This is the fallback content for _missing_')

