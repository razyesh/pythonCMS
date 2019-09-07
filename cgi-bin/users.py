#!/usr/bin/env python3
import db
from jinja2 import Environment, FileSystemLoader

def main():
    print("Content-Type:text\html\r\n\r\n")
    mycursor = db.mydb.cursor()
    sql_query = "select * from register"
    mycursor.execute(sql_query)
    users = mycursor.fetchall()

    file_loader = FileSystemLoader("admin")
    env = Environment(loader=file_loader)
    template = env.get_template('users.html')  
    output = template.render(users=users)
    print(output)

if __name__=='__main__':
    main()
