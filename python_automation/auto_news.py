# 구글 뉴스 사이트 기사 수집(RSS 활용) => 엑셀 시트로 정리
    # RSS(Rich Site Summary)

import feedparser
from urllib.parse import quote # 한글 키워드를 URL 인코딩
from openpyxl import Workbook
import ssl # RSS 주소가 SSL을 사용하는 주소일 때 필요하다.

keywords = ["경제", "과학기술", "건강"]
base_rss_url_pre = "https://news.google.com/rss/search?q=" 
base_rss_url_end = "&hl=ko&gl=KR&ceid=KR:ko"

urls = []

# 한글 키워드를 URL 인코딩 하여, 완성된 RSS 주소를 생성한다.
for keyword in keywords:
    urls.append(base_rss_url_pre + quote(keyword) + base_rss_url_end)

# print(urls)

# 새로운 엑셀 파일을 생성하기 위해 객체를 생성한다.
xlsx = Workbook()

# SSL 인증 과정을 생략할 수 있는 내용을 전달하도록 기본 내용을 변경한다.
ssl._create_default_https_context = ssl._create_unverified_context

for i in range(len(keywords)):
    sheet = xlsx.create_sheet(keywords[i]) # 키워드로 시트 생성
    sheet.append(['기사 제목', '링크', '날짜']) # 시트에 각 열의 제목을 추가

    news_list = feedparser.parse(urls[i]) # 딕셔너리 자료형으로 반환한다.
    # print(news_list)

    # items 태그의 내용들만 추출한다.
    for news in news_list['items']:
        # print(news)
        # 기사 제목, 링크, 날짜만 엑셀 시트에 기록한다.
        sheet.append([news['title'], news['link'], news['published']])

file_name = "news_list.xlsx"
xlsx.save(file_name) # 엑셀 파일 저장
print("파일 저장 완료 !")