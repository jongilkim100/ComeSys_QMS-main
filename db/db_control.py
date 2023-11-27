import sqlite3
con = sqlite3.connect('Y:/ComeSys_QMS/db/log.db')

cur = con.cursor()
cur.execute("CREATE TABLE log_data(이메일주소 TEXT, 로그인시간 TEXT ,로그아웃시간 TEXT);")
con.commit()
con.close() 
