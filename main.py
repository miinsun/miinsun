import feedparser
import time
import re
from bs4 import BeautifulSoup

# RSS 데이터 가져오기
URL = "https://miinsun.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 3

# 새로운 RSS 콘텐츠 생성
soup = BeautifulSoup("<p class='rss'></p>", "html.parser")
rss_tag = soup.find("p", class_="rss")

# RSS 피드 내용 추가
for idx, feed in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        formatted_date = f"{feed_date.tm_mon}/{feed_date.tm_mday}/{feed_date.tm_year}"

        # BeautifulSoup으로 a 태그 생성
        new_link = soup.new_tag("a", href=feed["link"], target="_blank")
        new_link.string = f"{formatted_date} - {feed['title']}"

        # 새로운 링크를 <p class="rss"> 안에 추가
        rss_tag.append(new_link)
        rss_tag.append(soup.new_tag("br"))
        
# 기존 README.md 파일 불러오기
try:
    with open("README.md", "r", encoding="utf-8") as file:
        content = file.read()

    # 기존 README를 BeautifulSoup으로 불러오기
    readme_soup = BeautifulSoup(content, "html.parser")
    old_rss_tag = readme_soup.find("p", class_="rss")

    # 기존 RSS 내용 삭제 후 새로운 내용 추가
    if old_rss_tag:
        old_rss_tag.replace_with(soup)

    # 변경된 README.md 다시 쓰기
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(str(readme_soup))

    print("README.md 업데이트 완료!")

except FileNotFoundError:
    print("README.md 파일이 없어서 새로 생성합니다.")
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(f'<p class="rss">{markdown_text}</p>')
