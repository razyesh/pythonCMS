#!/usr/bin/env python3
print("Content-Type:text/html\r\n\r\n")
import mysql.connector
import cgi, cgitb
import db
import hashlib

mycursor = db.mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS register( id int AUTO_INCREMENT PRIMARY KEY, username varchar(200) NOT NULL, email varchar(2000), password varchar(100));")


form= cgi.FieldStorage()
name = form.getvalue("username")
email = form.getvalue("email")
password = form.getvalue("password")
hash_password = hashlib.md5(str(password).encode())
id= None

sql = "insert into `register` VALUES(%s, %s, %s, %s)"
val =(name, email, hash_password.hexdigest(), id)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
mydb.close()
