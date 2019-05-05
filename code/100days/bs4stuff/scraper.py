#Python Shell Commands
#Day 2 - BeautifulSoup4

import bs4
import requests
import pprint

site = requests.get("https://kdnuggets.com")
site.raise_for_status()
soup = bs4.BeautifulSoup(site.text, 'html.parser')

#Search for first <ul> tag on the page
#x = soup.li
#print(x)

#Search for all <ul> tags on the page
y = soup.find_all('li')
pprint.pprint(y)

#Search for all <ul> tags within the <main> tag
#soup.main.ul

#Search for all <li> tags within the <main> tag and assign to variable
#all_li = soup.main.find_all('li')

#Print out the text data for all of the <li> tags (titles of URLs)
#for title in all_li:
#    print(title.string)