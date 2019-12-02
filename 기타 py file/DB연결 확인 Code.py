import pymysql.cursors  # sql사용을 위한 import
def connectDB(): #DB연결
    conn = pymysql.connect(host ="localhost", user = "root", password = "project", db = "projectl", charset = "utf8")

    return conn


def insertDB():
    conn = connectDB()
    with conn.cursor() as cursor:
        df.to_sql(name='real_time_top20', con=conn, if_exists='append')
        conn.close()

def selectDB(): #select문
    conn = connectDB()
    with conn.cursor() as cursor:
        sql = "select * from rental_history"
        cursor.execute(sql)
        prt = cursor.fetchall()
        print(prt)
        conn.close()

def main(): #실행 문
    insertDB()


main()