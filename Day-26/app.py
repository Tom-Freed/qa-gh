from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pass@localhost:3306/mydatabase'

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

@app.route('/')
def home():
    return "<h1>Homepage<h1>"

@app.route('/postoption', methods=['GET', 'POST'])
def posto():
    response = request.method
    return f"Method is {response}"

@app.route('/name/<name>/<int:num>')
def name(name, num):
    var1 = (name + '<br>') * num
    return var1

@app.route('/gotogoogle')
def gotogoogle():
    return redirect('http://www.google.com')

@app.route('/gotohome')
def gotohome():
    return redirect(url_for('home'))

@app.route('/squared/<int:num>')
def squared(num):
    return str(num**2)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)