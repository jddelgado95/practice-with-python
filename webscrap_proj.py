## We want to grab everything that's over 100 points in the https://news.ycombinator.com/ webpage.

## grab all the elements that have 'titleline class'. You can inspect the link and check if it has it. 

import requests ##Allowd us to donwload the HTML
from bs4 import BeautifulSoup ##allows to manipulate the HTMl and grab data
res = requests.get('https://news.ycombinator.com/news') ##gets the information 
soup = BeautifulSoup(res.text,'html.parser')
link = soup.select('.titleline') ##grabs the first element  titleline
votes = soup.select('.score')
##print(votes[0])

def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(link):

        title = link[idx].getText()
        href = link[idx].get('href', None)
        points = int(votes[idx].getText().replace(' points',''))
        print(points)
        hn.append({'title': title, 'link': href})
    return hn

print(create_custom_hn(link, votes))
