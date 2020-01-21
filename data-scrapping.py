import requests
from bs4 import BeautifulSoup

#get the data
url = requests.get('https://www.cicnews.com/feed')
coverpage = url.content

#load the data into bs4
# soup = BeautifulSoup(data.text, 'html.parser')
soup = BeautifulSoup(coverpage, 'html5lib')

# table = soup.find('table', {'class' : 'd3-o-table--row-striping'})
# tbody = table.find('tbody')

articles = soup.find_all('item')
print(articles[0].find('title'))
# matchup_items = tbody.findAll('tr')
# for item in matchup_items:
#     team_rank = item.find('p', {'class' : 'rank'}).text.strip()
#     team_name = item.find('span', {'class' : 'team-name'}).text.strip()
#     previous_rank = item.find('div', {'class' : 'pr-body'}).findAll('a')[0].text.strip()
#     print(team_rank + ', ' +team_name + ', ' + previous_rank)