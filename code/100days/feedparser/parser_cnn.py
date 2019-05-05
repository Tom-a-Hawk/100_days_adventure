import feedparser

FEED_FILE = "cnn10.xml"

feed = feedparser.parse(FEED_FILE)

if 'title' in feed.entries[0]:

    for entry in feed.entries:
            try:
                print(entry.published + " --- " + entry.category + ": " + entry.link)
            except:
                print("entry missing keyword")

else:
    print('no title')