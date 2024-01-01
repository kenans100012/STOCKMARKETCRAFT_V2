import  mysql.connector as connector
con =connector.connect(host='127.0.0.1', port='3306',
                  user ='root', password='Zaqws@2025',
                    database ='pythonstore')
print(con)