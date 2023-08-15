from flask import Flask, render_template, request, redirect, url_for
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
    quantity = db.Column(db.Integer, nullable=False)
    summary = db.Column(db.String, nullable=False) 
    basket = db.relationship('Basket', backref='stockbr')

class Basket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'),nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=False)

class QuantityForm(FlaskForm):
    stock_id = IntegerField('Stock ID')
    quantity = SelectField("Quantity", choices=[(1),(2),(3),(4),(5)])
    submit = SubmitField("Add to basket")

class BasketForm(FlaskForm):
    item_id = IntegerField('Item ID')
    quantity = SelectField("Quantity", choices=[(1),(2),(3),(4),(5)])
    update = SubmitField("Update")
    

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

    return render_template('products.html', stock=stock, form=form)

def add_to_basket(stock_id, qty):
    with app.app_context():
        stock = db.session.get(Stock, stock_id)
        if stock:
            basket_item = Basket(
                stock_id = stock_id, 
                quantity = qty,
                total = (stock.price * int(qty))
        )
        db.session.add(basket_item)
        stock.quantity -= int(qty)
        db.session.commit()


@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/basket', methods=["GET", "POST"])
def basket():
    basket = Basket.query.all()
    form = BasketForm()

    order_total = sum(item.total for item in basket)

    if request.method == "POST":
        if form.validate_on_submit():
            update_quantity = form.quantity.data
            item_id = form.item_id.data
            with app.app_context():
                update_item = db.session.get(Basket, item_id)
                if update_item:
                    update_item.quantity = update_quantity
                    update_item.total = int(update_quantity) * update_item.stockbr.price
                db.session.commit()

    return render_template('basket.html', basket=basket, form=form, order_total=order_total)

@app.route('/checkout', methods=["GET", "POST"])
def checkout():
    basket = Basket.query.all()

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