#!/usr/bin/env python3
print("Content-Type:text/html\r\n\r\n")
import db
import cgitb
cgitb.enable()
from jinja2 import Environment, FileSystemLoader
mycursor = db.mydb.cursor()
mycursor.execute("SELECT * FROM blog")
blog_list = mycursor.fetchall()

file_loader1 = FileSystemLoader("templates")
env1 = Environment(loader=file_loader1)
template1 = env1.get_template('blog.html')
output = template1.render(data=blog_list[::-1])
print(output)

    
    