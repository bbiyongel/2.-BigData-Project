import pandas as pd

user_rental = pd.read_pickle("rentlist1.pkl")

user_rental['rental_date'] = "2017-07-27"

from sqlalchemy import create_engine

# engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}".format(user="root",pw="project",db="testdb")) # 로컬 DB연결
engine = create_engine("mysql+pymysql://{user}:{pw}@121.67.246.142/{db}".format(user="project",pw="project",db="projectdb")) # 서버 DB 연결
user_rental.to_sql(con=engine, name='rental_history', if_exists='replace', index=False)