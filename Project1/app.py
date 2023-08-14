from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#pymysql
import os


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#"mysql+pymysql://root:pass@host/plant_stock"
#app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
#(In terminal) export DATABASE_URI=mysql+pymysql://username:password@host/database_name

db = SQLAlchemy(app)

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plant_name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class Basket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/product1')
def product1():
    return render_template('product1.html')

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)