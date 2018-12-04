from collections import namedtuple
import requests
import bs4
import pprint

# URL of site we want to scrape
URL = "https://news.ycombinator.com/"

def pull_site():
    raw_site_page = requests.get(URL) #Pull down the site.
    raw_site_page.raise_for_status()  #Confirm site was pulled. Error if not
    return raw_site_page

def scrape(site):
    header_list = []
    #Create BeautifulSoup object
    soup = bs4.BeautifulSoup(site.text, 'html.parser')
    html_header_list = soup.select('.title')

    for item in html_header_list:
        header_list.append(item.getText())

    #print(header_list)

    x = header_list[1::2]
    y = header_list[0::2]
    z = list(zip(y,x))

    for record in z:
        Article = namedtuple('Article', 'position title')
        article = Article(position=record[0], title=record[1])
        print(f'Article {article.position} is {article.title}')

if __name__ == "__main__":
    site = pull_site()
    scrape(site)