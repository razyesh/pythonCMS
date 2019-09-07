#!/usr/bin/env python3
print("Content-Type:text/html\r\n\r\n")
import db
import cgi

mycursor = db.mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS pages( id int AUTO_INCREMENT PRIMARY KEY, title varchar(200), content varchar(2000));")

form = cgi.FieldStorage()
title = form.getvalue("title")