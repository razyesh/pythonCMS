#!/usr/bin/env python3

import cgi, cgitb
from db import mydb
from jinja2 import Environment, FileSystemLoader
import db
print("Content-Type:text/html\r\n\r\n")


mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM register")
myresult = mycursor.fetchall()

number_of_post=0
mycursor.execute("SELECT * from blog")
posts = mycursor.fetchall()
for post in posts:
    number_of_post += 1

number_of_user = 0
for user in myresult:
    number_of_user += 1


form = cgi.FieldStorage()
file_loader = FileSystemLoader('admin')
env = Environment(loader=file_loader)
template = env.get_template('dashboard.html')

# for login

email = form.getvalue("email")
password = form.getvalue("password")

count=0
for x in myresult:
    if email == x[1] and password == x[2]:
        output = template.render(
            username=x[0], email=x[1], number_of_user=number_of_user, number_of_post=number_of_post, posts=posts)
        print(output)
        count=1
        break
    else:
        count=0

if count==0:
    print("<h3>Invalid Login Detail</h3>")
mydb.commit()
mydb.close()
