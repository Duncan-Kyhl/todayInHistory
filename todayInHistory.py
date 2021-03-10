# What Happened on this Day in History?

# import requests library for making HTTP requests
import requests
# import BeautifulSoup for getting data our of HTML request
from bs4 import BeautifulSoup
# import date for displaying dates
from datetime import date

# get request for website to be scraped
URL = 'https://www.britannica.com/on-this-day/March-10'
page = requests.get(URL)

# parse the webpage with BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# point to areas to be parsed
years = soup.find_all('div', attrs={'class': 'date-label position-absolute top-0 left-0 m-10 px-10 py-5 rounded bg-purple text-white font-weight-bold'})
events = soup.find_all('div', attrs={'class': 'card-body font-serif'})
# description = soup.find_all('div', attrs={'class': 'date-label position-absolute top-0 left-0 m-10 px-10 py-5 rounded bg-purple text-white font-weight-bold'})

# create lists of each parsed year and event title
listYears = []
listEvents = []

for each in years:
    listYears.append(each.text.strip())
for each in events:
    listEvents.append(each.text.strip())

# associate years:events
items = {}

for key in listYears:
    for value in listEvents:
            items[key] = value.split('.', 1)[0]
            listEvents.remove(value)
            break

    print(key)    # print out each year

# user selects a year
selection = input('Pick a year: ')

# get today's date
today = date.today().strftime("%B %d")

# display the historical event of today in the user selected year
print("On",today,selection,":")
print(items[selection],'.')