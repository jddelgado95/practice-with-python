## We want to grab everything that's over 100 points in the https://news.ycombinator.com/ webpage.

## grab all the elements that have 'titleline class'. You can inspect the link and check if it has it. 

import requests ##Allowd us to donwload the HTML
from bs4 import BeautifulSoup ##allows to manipulate the HTMl and grab data
import pprint


res = requests.get('https://news.ycombinator.com/news') ##gets the information 
soup = BeautifulSoup(res.text,'html.parser')
link = soup.select('.titleline') ##grabs the first element  titleline
subtext = soup.select('.subtext')
##print(votes[0])

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(link):
        title = link[idx].getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):            
            points = int(vote[0].getText().replace(' points',''))
            if points > 99:
                hn.append({'title': title, 'link': href,'votes':points})
    return hn

pprint.pprint(create_custom_hn(link, subtext))
