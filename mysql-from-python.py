import  os
import pymysql

#Gest username from ...

username =os.getenv("C9_User")
connection=pymysql.connect(host="localhost", user="root", password="6posr3Sb*", db="Chinook")

try:
    with connection.cursor() as cursor:
        sql="SELECT * FROM Artist;"
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result)
finally:
    connection.close()