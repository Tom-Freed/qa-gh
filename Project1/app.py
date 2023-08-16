from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, IntegerField, StringField, DateField
from wtforms.validators import DataRequired
from flask_bcrypt import Bcrypt
#pymysql
import os


app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
#(In terminal) export DATABASE_URI=mysql+pymysql://root:pass@localhost/project1
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

#"mysql+pymysql://root:pass@host/project1"


db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    summary = db.Column(db.String(1000), nullable=False) 
    basket = db.relationship('Basket', backref='stockbr')

class Basket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'),nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=False)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), nullable=False)
    card_num = db.Column(db.String(1000), nullable=False)
    expiry_month = db.Column(db.String(1000), nullable=False)
    expiry_year = db.Column(db.String(1000), nullable=False)
    cvc = db.Column(db.String(1000), nullable=False)

class QuantityForm(FlaskForm):
    stock_id = IntegerField('Stock ID')
    quantity = SelectField("Quantity", choices=[(1),(2),(3),(4),(5)])
    submit = SubmitField("Add to basket")

class BasketForm(FlaskForm):
    item_id = IntegerField('Item ID')
    quantity = SelectField("Quantity", choices=[(1),(2),(3),(4),(5)])
    update = SubmitField("Update")

class ShippingForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    address1 = StringField("Address line 1", validators=[DataRequired()])
    address2 = StringField("Address line 2", validators=[DataRequired()])
    postcode = StringField("Postcode", validators=[DataRequired()])
    payment = SubmitField("Proceed to payment")

class PaymentForm(FlaskForm):
    name = StringField("Cardholder's name", validators=[DataRequired()])
    card_num = IntegerField("Card number", validators=[DataRequired()])
    expiry_month = IntegerField("Expiry month", validators=[DataRequired()])
    expiry_year = IntegerField("Expiry year", validators=[DataRequired()])
    cvc = IntegerField("CVC", validators=[DataRequired()])
    buy_now = SubmitField("Buy now")
  
def initialise_database():
    with app.app_context():
        db.drop_all()
        db.create_all()
        plant1 = Stock(
            name='Plant1', 
            price=10.00, 
            quantity=10,
            summary = 'Plant 1 - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac varius nisi. Aliquam vitae diam tincidunt, porttitor erat lobortis, tincidunt felis. Aenean ultricies ligula nec neque interdum congue. Maecenas quis laoreet ligula. Mauris ornare laoreet erat eget porta. Donec gravida dui sit amet risus semper, vel pellentesque libero rhoncus. Fusce.'
        )
        plant2 = Stock(
            name='Plant2',
            price=11.25, 
            quantity=10,
            summary = 'Plant 2 - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac varius nisi. Aliquam vitae diam tincidunt, porttitor erat lobortis, tincidunt felis. Aenean ultricies ligula nec neque interdum congue. Maecenas quis laoreet ligula. Mauris ornare laoreet erat eget porta. Donec gravida dui sit amet risus semper, vel pellentesque libero rhoncus. Fusce.'
        )
        plant3 = Stock(
            name='Plant3', 
            price=12.50, 
            quantity=10,
            summary = 'Plant 3 - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac varius nisi. Aliquam vitae diam tincidunt, porttitor erat lobortis, tincidunt felis. Aenean ultricies ligula nec neque interdum congue. Maecenas quis laoreet ligula. Mauris ornare laoreet erat eget porta. Donec gravida dui sit amet risus semper, vel pellentesque libero rhoncus. Fusce.'
        )
        plant4 = Stock(
            name='Plant4', 
            price=13.75, 
            quantity=10,
            summary = 'Plant 4 - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac varius nisi. Aliquam vitae diam tincidunt, porttitor erat lobortis, tincidunt felis. Aenean ultricies ligula nec neque interdum congue. Maecenas quis laoreet ligula. Mauris ornare laoreet erat eget porta. Donec gravida dui sit amet risus semper, vel pellentesque libero rhoncus. Fusce.'
        )
        plant5 = Stock(
            name='Plant5', 
            price=14.00, 
            quantity=10,
            summary = 'Plant 5 - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac varius nisi. Aliquam vitae diam tincidunt, porttitor erat lobortis, tincidunt felis. Aenean ultricies ligula nec neque interdum congue. Maecenas quis laoreet ligula. Mauris ornare laoreet erat eget porta. Donec gravida dui sit amet risus semper, vel pellentesque libero rhoncus. Fusce.'
        )
        plant6 = Stock(
            name='Plant6',
            price=14.25,
            quantity=10,
            summary = 'Plant 6 - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac varius nisi. Aliquam vitae diam tincidunt, porttitor erat lobortis, tincidunt felis. Aenean ultricies ligula nec neque interdum congue. Maecenas quis laoreet ligula. Mauris ornare laoreet erat eget porta. Donec gravida dui sit amet risus semper, vel pellentesque libero rhoncus. Fusce.'
        )
        db.session.add_all([plant1, plant2, plant3, plant4, plant5, plant6])
        db.session.commit()

initialise_database()

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
    form = ShippingForm()

    order_total = sum(item.total for item in basket)

    if form.validate_on_submit():
        return render_template('checkout.html', basket=basket, order_total=order_total, form=form)

    return render_template('checkout.html', basket=basket, order_total=order_total, form=form)

@app.route('/payment', methods=["GET", "POST"])
def payment():
    form = PaymentForm()

    if request.method == "POST":
        if form.validate_on_submit():
            with app.app_context():
                new_payment = Payment(
                    name = form.name.data,
                    card_num = bcrypt.generate_password_hash(str(form.card_num.data)),
                    expiry_month = form.expiry_month.data,
                    expiry_year = form.expiry_year.data,
                    cvc =  bcrypt.generate_password_hash(str(form.cvc.data))
                )
                db.session.add(new_payment)
                db.session.commit()

                payments = Payment.query.all()
                return render_template('order_placed.html', payments=payments)

    return render_template('payment.html', form=form)

@app.route('/order_placed', methods=["GET", "POST"])
def order_placed():
    payments = Payment.query.all()
    return render_template("order_placed.html", payments=payments)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/product_page')
def product1():
    return render_template('product_page.html')

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)