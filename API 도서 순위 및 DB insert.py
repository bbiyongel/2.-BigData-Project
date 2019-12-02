import datetime # 4주간의 Top20 통계를 위한 API실시간을 위한 일자 처리

now = datetime.datetime.now() # 현재 일자
weeks4 = now + datetime.timedelta(weeks=-4) #현재 일자 - 4주
startDt = '%04d-%02d-%02d' % (weeks4.year, weeks4.month, weeks4.day)
endDt = '%04d-%02d-%02d' % (now.year, now.month, now.day) # 현재 일자에서 년,월,일만 출력되도록

apiKey = '비공개' #APIKey 변수

top10_url = "http://data4library.kr/api/loanItemSrch?authKey="+apiKey+"&startDt="+startDt+"&endDt="+endDt+"&pageSize=10"  # API호출 주소 top10_url변수에 저장

from bs4 import BeautifulSoup # 태그 파싱하기 위해 필요
from urllib.request import urlopen #Url주소를 불러오기 위해 필요

data = urlopen(top10_url).read() #top10_url을 읽어서 data변수에 저장
soup = BeautifulSoup(data, "html.parser") #BeautifulSoup를 통해 형식 parser
bookitem = soup.find("docs") # Tag에 docs태그를 찾아 bookitem에 저장

print(top10_url)

import pandas as pd

df = pd.DataFrame(columns=['book_rank', 'book_name', 'book_object_text', 'book_rental', 'book_isbn'])  # 빈 데이터 프레임 생성
i = 0  # i 초기값

genre = []
for items in bookitem.findAll("doc"):  # bookitem에 저장되어있는 docs태그에서 doc태그를 찾아서 items에 넣음
    a = items.class_no.text  # 카테고리를 a 라는 변수에 담는다.
    if a == "":  # 카테고리가 공백으로 나올 때
        a = "미분류"  # 미분류라고 넣어준다.
        genre.append(10)

    else:
        a = int(float(a))  # float형을 int형으로 변경 후 a에 다시 담고
        if 0 <= a < 99:
            a = "총류"
            genre.append(0)
        elif 100 <= a < 200:
            a = "철학"
            genre.append(1)
        elif 200 <= a < 300:
            a = "종교"
            genre.append(2)
        elif 300 <= a < 400:
            a = "사회과학"
            genre.append(3)
        elif 400 <= a < 500:
            a = "자연과학"
            genre.append(4)
        elif 500 <= a < 600:
            a = "기술과학"
            genre.append(5)
        elif 600 <= a < 700:
            a = "예술"
            genre.append(6)
        elif 700 <= a < 800:
            a = "언어"
            genre.append(7)
        elif 800 <= a < 900:
            a = "문학"
            genre.append(8)
        else:
            a = "역사"
            genre.append(9)

    df.loc[i] = [items.ranking.text, items.bookname.text, a, items.loan_count.text, items.isbn13.text]
    i = i + 1

# 0총류 1철학 2종교 3사회과학 4자연과학 5기술과학 6예술 7언어 8문학 9역사 10미분류
df["book_isbn_code"] = genre
print(df)

from pandas.io import sql
from sqlalchemy import create_engine

# engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}".format(user="root",pw="project",db="testdb"))  # 로컬 DB 연결 방법
engine = create_engine("mysql+pymysql://{user}:{pw}@121.67.246.142/{db}".format(user="project",pw="project",db="projectdb"))  # 서버 DB 연결 방법
df.to_sql(con=engine, name='api_top10', if_exists='replace', index=False)
