## We want to grab everything that's over 100 points in the https://news.ycombinator.com/ webpage.

## grab all the elements that have 'titleline class'. You can inspect the link and check if it has it. 

import requests ##Allowd us to donwload the HTML
from bs4 import BeautifulSoup ##allows to manipulate the HTMl and grab data
import pprint


res = requests.get('https://news.ycombinator.com/news') ##gets the information
res2 = requests.get('https://news.ycombinator.com/news?p=2') ## here we want to scrap two pages of the webpage
soup = BeautifulSoup(res.text,'html.parser')
soup2 = BeautifulSoup(res2.text,'html.parser')
link = soup.select('.titleline') ##grabs the first element  titleline
subtext = soup.select('.subtext')
link2 = soup2.select('.titleline') ##grabs the first element  titleline
subtext2 = soup2.select('.subtext')
##print(votes[0])

mega_links = link + link2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key = lambda k:k['votes'], reverse=True)

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
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))
