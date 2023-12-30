#DL_register
import mysql.connector
from mysql.connector import Error
import os
dir=r"D:\Shaun\Documents\Comp_Project"
os.chdir(dir)
e=Error
def DL_register_main(access_mode,email_id,user_id,first_name,last_name,Error_code):
    def connect(email_id,user_id,first_name,last_name,Error_code):
      Error_code=None
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
               print(cursor.fetchall())

        if access_mode=="READONE":
               print("enter readone",email_id)
               cursor=conn.cursor()
               select_query="SELECT User_ID from sa_register where EMAIL = %s"
               cursor.execute(select_query,(email_id,))
               res=cursor.fetchone()
               print(res)
               if res is None:
                  Error_code=1
               else:
                  user_id=res[0]

      except Error as e:
        Error_code = f"Error: {e.args[0]}"
      finally:
        if conn is not None and conn.is_connected():
            conn.close()
        return(email_id,user_id,first_name,last_name,Error_code)
    email_id,user_id,first_name,last_name,Error_code=connect(email_id,user_id,first_name,last_name,Error_code)
    return(access_mode,email_id,user_id,first_name,last_name,Error_code)    