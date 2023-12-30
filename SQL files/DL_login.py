#DL_login
import mysql.connector
from mysql.connector import Error
import os
dir=r"D:\Shaun\Documents\Comp_Project"
os.chdir(dir)
e=Error
def DL_login_main(access_mode,user_id,passw,Error_code):
    def connect(user_id,passw,Error_code):
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
               insert_query="INSERT INTO sa_login (User_ID,Passwd) VALUES (%s,%s)"
               cursor.execute(insert_query,(user_id,passw))
               conn.commit()
               print(cursor.fetchall())
            if access_mode=="READONE":
               cursor=conn.cursor()
               select_query="SELECT Passwd from sa_login where User_ID = %s"
               cursor.execute(select_query,(user_id,))
               res=cursor.fetchone()
               if res is None:
                  Error_code=1
               else:
                  passw=res[0]
            if access_mode=="UPDATE":
               cursor=conn.cursor()
               update_query="UPDATE sa_login set passwd = %s where User_ID = %s"
               cursor.execute(update_query,(passw,user_id))
               conn.commit()
               print(passw,user_id)
                         
      except Error as e:
        print(e)
        Error_code = f"Error: {e.args[0]}"
      finally:
        if conn is not None and conn.is_connected():
            conn.close()
        return(user_id,passw,Error_code)
    user_id,passw,Error_code=connect(user_id,passw,Error_code)   
    return(access_mode,user_id,passw,Error_code)