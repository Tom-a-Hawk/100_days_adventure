import requests

URL = "http://rss.cnn.com/services/podcasting/cnn10/rss.xml"

if __name__ == '__main__':
    r = requests.get(URL)
    with open('cnn10.xml', 'wb') as fin:
        fin.write(r.content)