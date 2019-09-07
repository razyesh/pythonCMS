#!/usr/bin/env python3
import cgitb
import cgi
import mysql.connector


def main():
    print("Content-Type:text/html\r\n\r\n")


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pythoncms"
)

if __name__ == "__main__":
    main()
