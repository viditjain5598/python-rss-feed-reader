import feedparser as fp

def parse(url):
    return fp.parse(url)

def get_source(feed_obj):
    feed = feed_obj['feed']
    return {
            'link': feed['link'],
            'title': feed['title'],
            'subtitle': feed['subtitle'],
            }

def get_articles(feed_obj):
    entries = feed_obj['entries']
    articles = []
    for entry in entries:
        articles.append({
            'id':entry['id'],
            'link':entry['link'],
            'title':entry['title'],
            'summary':entry['summary'],
            'published':entry['published_parsed'],
            })
    return articles
