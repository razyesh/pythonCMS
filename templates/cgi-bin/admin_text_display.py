#!/usr/bin/env python3
print("Content-Type:text/html\r\n\r\n")
import db
from jinja2 import Environment, FileSystemLoader
mycursor = db.mydb.cursor()
mycursor.execute("SELECT * FROM blog")
blog_list = mycursor.fetchall()

file_loader2 = FileSystemLoader("admin")
env2 = Environment(loader=file_loader2)
template2 = env2.get_template('posts.html')
output = template2.render(datas=blog_list[::-1])
print(output)
    
    