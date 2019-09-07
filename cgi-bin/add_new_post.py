#!/usr/bin/env python3
print("Content-Type: text/html")
print()
import db
import cgi 
from jinja2 import Environment, FileSystemLoader


mycursor = db.mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS blog( id int AUTO_INCREMENT PRIMARY KEY, title varchar(200), content varchar(2000), meta_description varchar(300), published bit, publish_date date);")
form = cgi.FieldStorage()
file_loader = FileSystemLoader('admin')
env = Environment(loader=file_loader)
template = env.get_template('add.html')

id = None
title = form.getvalue("title")
content = form.getvalue("content")
date = form.getvalue("date")
tags = form.getvalue("tags")
meta = form.getvalue("meta")
publish = form.getvalue("publish")

if publish=="on":
    publish = True
else:
    publish = False

def blog_content(title, content, date, tags, meta, publish):
    sql = "insert into `blog` values(%s, %s,%s, %s, %s, %s, %s)"
    val = (title, content, date, id, tags, meta, publish)
    mycursor.execute(sql, val)

blog_content(title, content, date, tags, meta, publish)

db.mydb.commit()
message = f"{mycursor.rowcount} Blog Published"
print(message)
db.mydb.close()
