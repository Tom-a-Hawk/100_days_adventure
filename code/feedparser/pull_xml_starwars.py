import requests

URL = "http://www.galacticbinder.com/podcast-feed/sarlaccpit.xml"

if __name__ == '__main__':
    r = requests.get(URL)
    with open('starwars.xml', 'wb') as fin:
        fin.write(r.content)