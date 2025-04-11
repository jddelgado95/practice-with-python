## newspaper3k is a python library for extracting and curating articles

import newspaper 

url ='https://edition.cnn.com/2025/04/10/politics/trump-xi-china-tariffs/index.html'
article = newspaper.Article(url)
article.download()
print(article.html)
article.parse() ##deconstruct article objects
print(article.authors)
print(article.publish_date)
print(article.text)
print(article.top_image)

cnn = newspaper.build('http://cnn.com')

for a in cnn.article[:10]
    print(a)

for c in cnn.category_urls():
    print(c)

## cnn_article = cnn.article[0] ## creates an object based on the first cnn article
## cnn_article.download()
## cnn_article.html
# cnn.article.parse()
# print(cnn_article.title)
# 
# 
# How to perform NLP

cnn_article.nlp()

cnn_article.keywords()

cnn_article.summary()

    