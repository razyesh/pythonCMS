#!/usr/bin/env python3
print("Content-Type:text/html\r\n\r\n")
import mysql.connector
import cgi, cgitb
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="pythoncms",
    charset='utf8mb4',
)

mycursor = mydb.cursor()
form= cgi.FieldStorage()
name = form.getvalue("username")
email = form.getvalue("email")
password = form.getvalue("password")
print(f"<h1>{name}</h1>")
print(f"<h1>{email}</h1>")
id= None

sql = "insert into `register` VALUES(%s, %s, %s, %s)"
val =(name, email, password, id)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
mydb.close()
