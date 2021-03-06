import requests
from bs4 import BeautifulSoup

#get the data
url = requests.get('https://www.cicnews.com/feed')
coverpage = url.content

soup = BeautifulSoup(coverpage, 'html5lib')
articles = soup.find_all('item')

print(articles[0].find('title').get_text(strip=True))
print(articles[1].find('title').get_text(strip=True))


#load the data into bs4
# soup = BeautifulSoup(data.text, 'html.parser')

# table = soup.find('table', {'class' : 'd3-o-table--row-striping'})
# tbody = table.find('tbody')

# matchup_items = tbody.findAll('tr')
# for item in matchup_items:
#     team_rank = item.find('p', {'class' : 'rank'}).text.strip()
#     team_name = item.find('span', {'class' : 'team-name'}).text.strip()
#     previous_rank = item.find('div', {'class' : 'pr-body'}).findAll('a')[0].text.strip()
#     print(team_rank + ', ' +team_name + ', ' + previous_rank)