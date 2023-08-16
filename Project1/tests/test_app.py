from flask_testing import TestCase
from app import app, db, bcrypt, Stock, Basket, Payment
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app
    
    def setUp(self):
        db.create_all()
        stock_test = Stock(
            name = "test", 
            price = 10.00, 
            quantity = 10,
            summary = 'Test - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac varius nisi. Aliquam vitae diam tincidunt, porttitor erat lobortis, tincidunt felis. Aenean ultricies ligula nec neque interdum congue. Maecenas quis laoreet ligula. Mauris ornare laoreet erat eget porta. Donec gravida dui sit amet risus semper, vel pellentesque libero rhoncus. Fusce.'
        )
        
        basket_test = Basket(
            stock_id = stock_test.id, 
            quantity = 2,
            total = (stock_test.price * int(2))
        )

        payment_test = Payment(
            name = "test",
            card_num = bcrypt.generate_password_hash(str(123)),
            expiry_month = 8,
            expiry_year = 23,
            cvc =  bcrypt.generate_password_hash(str(456))
        )
        db.session.add(stock_test, basket_test)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_products_get(self):
        response = self.client.get(url_for('products'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"test", response.data)
    
    def test_categories_get(self):
        response = self.client.get(url_for('categories'))
        self.assertEqual(response.status_code, 200)
    
    def test_basket_get(self):
        response = self.client.get(url_for('basket'))
        self.assertEqual(response.status_code, 200)
        
    def test_checkout_get(self):
        response = self.client.get(url_for('checkout'))
        self.assertEqual(response.status_code, 200)
    
    def test_payment_get(self):
        response = self.client.get(url_for('payment'))
        self.assertEqual(response.status_code, 200)
    
    def test_orderplaced_get(self):
        response = self.client.get(url_for('order_placed'))
        self.assertEqual(response.status_code, 200)
    
    def test_contact_get(self):
        response = self.client.get(url_for('contact'))
        self.assertEqual(response.status_code, 200)
    
    def test_about_get(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)
    
    def test_productpage_get(self):
        response = self.client.get(url_for('product_page'))
        self.assertEqual(response.status_code, 200)
        