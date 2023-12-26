#DL_login
import mysql.connector
from mysql.connector import Error
import os
dir=r"D:\Shaun\Documents\Comp_Project"
os.chdir(dir)
e=Error
def DL_login_main(access_mode,user_id,passw,Error_code):
    def connect():
      conn = None
      try:
        conn = mysql.connector.connect(host='127.0.0.1',
                                       database='stockapp',
                                       user='stockboi',
                                       password='shaunjosephn@gmail.com')
        if conn.is_connected():
            print('Connected to MySQL database')
            if access_mode=="INSERT":
               cursor=conn.cursor()
               insert_query="INSERT INTO sa_login (User_ID,Password) VALUES (%s,%s,)"
               cursor.execute(insert_query,(user_id,passw))
               conn.commit()
               print(cursor.fetch(1))


      except Error as e:
        print(e)
        print(e.args[0])
      finally:

        if conn is not None and conn.is_connected():
            print(conn.is_connected())
            conn.close()
    connect()   
    return(access_mode,user_id,passw,Error_code)