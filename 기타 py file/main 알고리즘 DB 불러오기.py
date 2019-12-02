import pymysql.cursors  # sql사용을 위한 import
import pandas as pd
import time

import time
start_vect=time.time()

# DB 연결
# autocommit(query 실행 후 자동 commit 명령어 실행) - DB 반영부분
# cursor class DB를 조회한 결과를 column 명이 key 인 dictionary 저장
# connection = pymysql.connect(host ="localhost", user = "root", password = "project", db = "testdb", charset = "utf8", autocommit = True, cursorclass=pymysql.cursors.DictCursor) #로컬 DB연결
connection = pymysql.connect(host ="121.67.246.142", user = "project", password = "project", db = "projectdb", charset = "utf8", autocommit = True, cursorclass=pymysql.cursors.DictCursor) #서버 DB연결

cursor = connection.cursor()
sql = "select * from rental_history"
cursor.execute(sql)

result = cursor.fetchall()
connection.close()

df = pd.DataFrame(result)

del df['rental_date']
print(df.head(5))

print("training Runtime: %0.2f Minutes"%((time.time() - start_vect)/60))