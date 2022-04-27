from crypt import methods
from flask import Flask, request
import pymysql
from app import app
from db import mysql
import json



@app.route('/',methods=['GET'])
def home():
   return ('hello world!')


@app.route('/posts', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        firstname = request.json['firstname']
        lastname = request.json['lastname']
        email = request.json['email']
        phone = request.json['phone']
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("INSERT INTO USERS(firstName, lastName, email, phone) VALUES (%s, %s, %s, %s)", (firstname, lastname, email, phone))
        mysql.connect.commit()
        cur.close()
        return 'success'

@app.route('/users')
def display():
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute('SELECT * FROM USERS')
        users = cur.fetchall() 
        usersObj = json.dumps(users)
        return usersObj
        #return users


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)