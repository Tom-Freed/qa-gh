from app import db, app, Orders, Products, Order_Products

with app.app_context():
    db.drop_all()
    db.create_all()