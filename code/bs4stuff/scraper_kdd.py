import requests
import bs4
import pprint

# URL of site we want to scrape
URL = "https://kdnuggets.com"

def pull_site():
    raw_site_page = requests.get(URL) #Pull down the site.
    raw_site_page.raise_for_status()  #Confirm site was pulled. Error if not
    return raw_site_page

def scrape(site):
    header_list = []
    #Create BeautifulSoup object
    soup = bs4.BeautifulSoup(site.text, 'html.parser')
    html_header_list = soup.select('ol.three_ol')

    for item in html_header_list[:1]:
        header_list.append(item.getText())

    print("The 7 most popular articles on KDNuggets.com at this time are:")
    print(header_list[0])



if __name__ == "__main__":
    site = pull_site()
    scrape(site)