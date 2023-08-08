from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
import os

app = Flask(__name__) # Declare Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI") # Set the connection string to connect to a database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) # Declare SQLAlchemy object

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(30), nullable=False)
    order_products = db.relationship('Order_Products', backref='orders')

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(30), nullable=False)
    order_products = db.relationship('Order_Products', backref='products')

class Order_Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column('order_id', db.Integer, db.ForeignKey('orders.id'))
    product_id = db.Column('product_id', db.Integer, db.ForeignKey('products.id'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)