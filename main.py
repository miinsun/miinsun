import feedparser
import time
import re

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
        markdown_text += (
            f'<p> {feed_date.tm_mon}/{feed_date.tm_mday} - '
            f'<a href="{feed["link"]}" target="_blank">{feed["title"]}</a></p>\n'
        )

# 기존 README.md 파일 불러오기
try:
    with open("README.md", "r", encoding="utf-8") as file:
        content = file.read()

    # <p class="rss"> 태그 안 내용 대체 (기존 내용 유지)
    updated_content = re.sub(
        r'(<p class="rss">)(.*?)(</p>)',
        rf'\1{markdown_text}\3',
        content,
        flags=re.DOTALL
    )

    # 변경된 내용 다시 쓰기
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(updated_content)

    print("README.md 업데이트 완료!")

except FileNotFoundError:
    print("README.md 파일이 없어서 새로 생성합니다.")
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(f'<p class="rss">{markdown_text}</p>')
