from operator import indexOf
from traceback import print_tb

from bs4 import BeautifulSoup
import requests

# with open('website.html', 'r') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# url = soup.select_one("h3", class_='heading')

hacker_website = requests.get('https://news.ycombinator.com/').text

soup = BeautifulSoup(hacker_website, 'html.parser')

select = soup.select('tr td span a', class_='athing_submission title titleline')

filtr = [i for i in select if i.get('href', '').startswith('https://')]

filtered = []

for element in filtr:
    filtered.append(element)

article_name = filtered[0].getText()
article_link = filtered[0]['href']

names = [element.getText() for element in filtered]
links = [element['href'] for element in filtered]

#srticle score
select2 = soup.select('td span span', class_='subtext subline score')
scores = [int(s.getText().split(' ')[0]) for s in select2 if s.get('id', '').startswith('score_')]
article_score = scores[0]

print(names)
print(links)
print(scores)


highest_score = scores.index(max(scores))

print(names[highest_score])
print(scores[highest_score])
print(links[highest_score])