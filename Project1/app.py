from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, IntegerField
#pymysql
import os


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

#"mysql+pymysql://root:pass@host/plant_stock"
#app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
#(In terminal) export DATABASE_URI=mysql+pymysql://username:password@host/database_name

db = SQLAlchemy(app)

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    summary = db.Column(db.String, nullable=False) 
    basket = db.relationship('Basket', backref='basketbr')

class Basket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'),nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=False)

class QuantityForm(FlaskForm):
    stock_id = IntegerField('Stock ID')
    quantity = SelectField("Quantity", choices=[(1),(2),(3),(4),(5)])
    submit = SubmitField("Add to basket")


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products', methods=["GET", "POST"])
def products():
    stock = Stock.query.all()
    form = QuantityForm()

    if request.method == "POST":
        if form.validate_on_submit():
            quantity = form.quantity.data
            stock_id = form.stock_id.data
            form.quantity.data = 1
            add_to_basket(stock_id, quantity)

    return render_template('products.html', stock=stock, form=form)

def add_to_basket(plant_id, qty):
    with app.app_context():
        stock = db.session.get(Stock, plant_id)
        if stock:
            basket_item = Basket(
                stock_id = plant_id, 
                price = stock.price,
                quantity = qty,
                total = (stock.price * int(qty))
        )
        db.session.add(basket_item)
        db.session.commit()


@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/basket')
def basket():
    basket = Basket.query.all()
    return render_template('basket.html', basket=basket)

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