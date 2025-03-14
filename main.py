import feedparser
import time
import re
from bs4 import BeautifulSoup

# RSS 데이터 가져오기
URL = "https://miinsun.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = ""

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        formatted_date = f"{feed_date.tm_mon}/{feed_date.tm_mday}/{feed_date.tm_year}"
        markdown_text += f' -<a href="{feed["link"]}" target="_blank">({formatted_date}) {feed["title"]}</a>'
        
# 기존 README.md 파일 불러오기
try:
    with open("README.md", "r", encoding="utf-8") as file:
        content = file.read()

    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(content, "html.parser")

    # <p class="rss"> 태그를 찾아서 해당 내용만 업데이트
    rss_tag = soup.find("p", class_="rss")
    if rss_tag:
        rss_tag.clear()  # 기존 내용 삭제
        rss_tag.append(markdown_text)  # 새로운 내용 추가

    # 기존 내용과 변경된 내용을 합쳐서 다시 쓰기
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(str(soup))  # 수정된 HTML을 그대로 저장

    print("README.md 업데이트 완료!")

except FileNotFoundError:
    print("README.md 파일이 없어서 새로 생성합니다.")
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(f'<p class="rss">{markdown_text}</p>')
