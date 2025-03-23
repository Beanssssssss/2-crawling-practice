from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from collections import Counter
import re
import time

# Selenium 드라이버 설정 (Chrome 사용)
driver = webdriver.Chrome()

# Yanolja 리뷰 페이지로 이동
url = 'https://www.yanolja.com/reviews/domestic/3015391'
######## your code here ########
driver.get(url)

# 페이지 로딩을 위해 대기
time.sleep(3)

# 스크롤 설정: 페이지 하단까지 스크롤을 내리기
scroll_count = 10  # 스크롤 횟수 설정
for _ in range(scroll_count):
    ######## your code here ########
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)  # 스크롤 이후 대기

# 웹페이지 소스 가져오기
page_source = driver.page_source

# BeautifulSoup를 사용하여 HTML 파싱
soup = BeautifulSoup(page_source, 'html.parser')
# 리뷰 텍스트 추출

reviews_class = soup.find_all("p", class_=["context-text", "css-c92dc4"])  # `class_` 속성 사용
# 심심해서 리뷰어도 추출
reviews = []
reviewers_class = []
reviewer_parents = soup.find_all("p", class_=["css-1irbwe1"])
for parent in reviewer_parents:
    span = parent.find("span")  # <p> 내부의 <span> 찾기
    if span:
        reviewers_class.append(span.text)

# 리뷰어 리스트 출력
# 각 리뷰 텍스트 정리 후 추가
for review, reviewer in zip(reviews_class, reviewers_class) :
    cleaned_text = review.get_text(strip=True).replace('\r', '').replace('\n', '')
    reviews.append(f"{reviewer} : {cleaned_text}")
ratings = []

rating_containers = soup.find_all("svg", attrs={"xmlns": "http://www.w3.org/2000/svg", "class": "css-1mj121y"})

count = 0
rating = 0

for container in rating_containers:
    if count == 5:
        ratings.append(rating)
        count = 0
        rating = 0

    path_tag = container.find("path")
    if path_tag:
        d_attr = path_tag['d']
        star_check = d_attr[1:3] 

        # 너의 기준에 맞게 판단
        if star_check.startswith('12'):  # 별이 채워진 경우로 간주
            rating += 1

    count += 1

# 마지막 리뷰 처리 (남은 게 있을 경우)
if count > 0:
    ratings.append(rating)

# 별점과 리뷰를 결합하여 리스트 생성
data = list(zip(ratings, reviews))

# DataFrame으로 변환
df_reviews = pd.DataFrame(data, columns=['Rating', 'Review'])

# 평균 별점 계산
average_rating = sum(ratings) / len(ratings)

# 불용어 리스트 (한국어)
korean_stopwords = set(['이', '그', '저', '것', '들', '다', '을', '를', '에', '의', '가', '이', '는', '해', '한', '하', '하고', '에서', '에게', '과', '와', '너무', '잘', '또','좀', '호텔', '아주', '진짜', '정말'])

# 모든 리뷰를 하나의 문자열로 결합
all_reviews_text = " ".join(reviews)

# 단어 추출 (특수문자 제거)
words = re.sub(r'[^가-힣a-zA-Z0-9\s]', '', all_reviews_text).split()

# 불용어 제거
filtered_words = [c for c in words if c not in korean_stopwords]

# 단어 빈도 계산
word_counts = Counter(filtered_words)

# 자주 등장하는 상위 15개 단어 추출
common_words = word_counts.most_common(15)
summary_df = pd.DataFrame({
    'Average Rating': [average_rating],
    'Common Words': [', '.join([f"{word}({count})" for word, count in common_words])]
})

# 최종 DataFrame 결합
final_df = pd.concat([df_reviews, summary_df], ignore_index=True)
# Excel 파일로 저장
final_df.to_excel("final.xlsx", index = False)
# 드라이버 종료
driver.quit()