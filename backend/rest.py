from crypt import methods
from flask import Flask, request, make_response, jsonify
import pymysql
from app import app
from db import mysql
import json
from flask_cors import CORS,cross_origin


cors = CORS(app, resources={r"/backend/*": {"origins": "*"}}) #Alt: Allow single path CORS with @cross_origin()



@app.route('/backend/v1.0/posts', methods=['GET', 'POST', 'PUT'])
def index():
    if request.method == "POST":
        try:
            firstname = request.json['firstname']
            lastname = request.json['lastname']
            email = request.json['email']
            phone = request.json['phone']
            conn = mysql.connect()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("INSERT INTO USERS(firstName, lastName, email, phone) VALUES (%s, %s, %s, %s)", (firstname, lastname, email, phone))
            mysql.connect.commit()
            cur.close()
            sample_response = {
                "result": 'sucess'
            }
        except Exception as e:
            sample_response = {
                "result": 'failed',
                "error": str(e)
            }
        return sample_response
    else:
        sample_response = {"result": 'failed'}
    # JSONify response
    response = make_response(jsonify(sample_response))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/backend/v1.0/users')
def display():
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute('SELECT * FROM USERS')
        users = cur.fetchall() 
        usersObj = json.dumps(users)
        response = make_response(jsonify(users))
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = 'application/json'
        return response
        #return users


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)