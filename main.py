import feedparser
import time
URL="https://dev-wnstjd.tistory.com/rss" # URL = "내블로그 주소/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
<h3> Latest Tistory Posting </h3>
"""

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f" <p> [{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']})</p>"

print(markdown_text)

f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)

f.close()
