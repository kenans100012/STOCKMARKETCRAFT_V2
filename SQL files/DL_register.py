#DL_register
import mysql.connector
from mysql.connector import Error
import os
dir=r"D:\Shaun\Documents\Comp_Project"
os.chdir(dir)
e=Error
def DL_register_main(access_mode,email_id,user_id,first_name,last_name,Error_code):
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
               insert_query="INSERT INTO sa_register (Email,User_ID,First_Name,Last_Name) VALUES (%s,%s,%s,%s)"
               cursor.execute(insert_query,(email_id,user_id,first_name,last_name))
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
    return(access_mode,email_id,user_id,first_name,last_name,Error_code)