import random
import string
import pandas as pd
import csv

csv_colums = ['회원번호', '회원이름', '비밀번호', '나이', '성별', '관심분야']

# 가장 많은 성 10개 중 한 개를 선별 이름엔 들어갈 땐 랜덤으로 설정됨.
first_name = ['김', '이', '박', '최', '정', '강', '조', '윤', '장', '임']
name = string.ascii_uppercase

# csv 파일 오픈, 덮어쓰기를 위해 'w'를 사용
# newline은 줄 바꿈을 위해 사용
# 한글 깨짐 방지를 위해 encoding euc-kr 사용
with open('tuser1.csv', 'w', newline='', encoding='euc-kr') as f:
    writer = csv.DictWriter(f, fieldnames=csv_colums)
    writer.writeheader()

    # 회원 테이블을 만들기 위해 Dictionary 형태로 만들어줌(test : 100명)
    for i in range(1, 130001):
        result = ""  # 결과 값
        for a in range(1, 4):
            if (a == 1):
                result += random.choice(first_name)  # 랜덤한 문자열 하나 선택
            else:
                result += random.choice(string.ascii_lowercase)

        # ID,이름,나이,성별,관심분야에 랜덤 데이터 값 저장
        dict1 = {'회원번호': i, '회원이름': result, '비밀번호': 1234, '나이': random.randrange(8, 65), '성별': random.randrange(0, 2),
                 '관심분야': random.randrange(0, 9)}

        # 한개씩 밑으로 저장
        writer.writerow(dict1)

tuser = pd.read_csv('tuser1.csv', encoding='euc-kr')
tuser1 = tuser[['회원번호', '회원이름', '비밀번호', '나이', '성별', '관심분야']]
tuser1