import json
from flask import Flask, request, render_template
from flask_cors import CORS
import pymongo
import redis

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
app = Flask(__name__)
CORS(app)


@app.route('/insert', methods=['POST'])
def register_api():
    mycol = mydb["farm_customers"]
    data = request.json
    data_ins = {"name": data["name"], "username": data["username"], "password": data["password"]}
    print(data_ins)
    mystery = {"username": data["username"]}
    macon = mycol.find(mystery)
    temp = []
    for x in macon:
        temp.append(x)
    if not temp:
        x = mycol.insert_one(data_ins)
    else:
        data = json.dumps({"status": "already present"})
    return data


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/register', methods=['GET'])
def register():
    return render_template("register.html")


@app.route('/login', methods=['GET'])
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
