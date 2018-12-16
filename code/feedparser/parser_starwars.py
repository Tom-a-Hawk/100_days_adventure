import feedparser

FEED_FILE = "starwars.xml"

feed = feedparser.parse(FEED_FILE)

if 'title' in feed.entries[0]:

    for entry in feed.entries:
            try:
                print(entry.published + " - " + entry.title + ": " + entry.link)
            except:
                print("entry missing keyword")

else:
    print('no title')