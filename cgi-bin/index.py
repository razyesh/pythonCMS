#!/usr/bin/env python3
from jinja2 import Environment, FileSystemLoader
print("Content-Type:text/html\r\n\r\n")
import cgi, cgitb
form= cgi.FieldStorage()
import webbrowser
url = "http://localhost/python/profile.html"
print("<html>")
print("<body>")
print("<h1>Welcome to Python Web programming</h1>")
print("<h2>Oh great</h2>")
print("</body>")
print("</html>")
content = 'This is homepage'
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('app.html')
output = template.render(content=content)
print(output)

