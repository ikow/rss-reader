import feedparser


class HandleRequest:
    def __init__(self):
        self.url = 'http://xuanwulab.github.io/cn/secnews/atom.xml'
        self.feed = feedparser.parse(self.url)

    def print_title(self):
        print self.feed.feed.title
        return

    def rss_feed(self):
        return self.feed

'''
t = HandleRequest()
#t.print_title()
print t.feed.feed.title
for item_rss in t.feed['items']:
    print item_rss.title
    print item_rss.description
'''

