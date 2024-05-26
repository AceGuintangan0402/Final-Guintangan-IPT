from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL
from flask_httpauth import HTTPBasicAuth
import dicttoxml


app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "cars"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"


mysql = MySQL(app)

auth = HTTPBasicAuth()


users = {
    "user1": "password1",
    "user2": "password2"
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username
    return None

def convert_to_xml(data):
    xml = dicttoxml.dicttoxml(data, custom_root='response', attr_type=False)
    return xml

@app.route("/")

def hello_world():
    
    style = """
        <style>
            p {
                font-family: Arial, sans-serif;
                font-size: 50px;
                color: blue;
                text-align: center;
                
            }
        </style>
    """
    return f"{style} <p>WELCOME TO ACE DATABASE</p>"