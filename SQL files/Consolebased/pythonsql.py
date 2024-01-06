import  mysql.connector as connector

class DBhelper: #class
    def __init__(self): #constructor
        #creation of mysql connector
        self.con =connector.connect(host='127.0.0.1', port='3306',
                                    user ='root', password='Zaqws@2025',
                                    database ='pythonstore')
        query ='create table if not exists user(userId varchar(200) primary key, emailId varchar(200), first_name varchar(200), last_name varchar(200), password varchar(200))'
        
        cur = self.con.cursor()
        cur.execute(query)
        #print("Query created")
        
    #insert
    def insert_user(self, userid, emailid,firstname,lastname,password1):
        query = "insert into user(userId, emailId, first_name, last_name, password) values({},'{}','{}','{}','{}')".format(userid,emailid,firstname,lastname,password1)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        #print("USER HAS BEEN ADDED")
    
    #fetching data
    def fetch_all(self):
        fetchdata = []
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            fetchdata.append(row)
        #print(fetchdata)
        return fetchdata
       
#main coding:
helper = DBhelper()
