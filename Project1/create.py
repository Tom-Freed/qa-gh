from app import db, app, Stock

with app.app_context():
    db.drop_all()
    db.create_all()
    plant1 = Stock(name='Plant1', price=10.00, stock=10)
    plant2 = Stock(name='Plant2', price=11.25, stock=10)
    plant3 = Stock(name='Plant3', price=12.50, stock=10)
    plant4 = Stock(name='Plant4', price=13.75, stock=10)
    plant5 = Stock(name='Plant5', price=14.00, stock=10)
    db.session.add_all([plant1, plant2, plant3, plant4, plant5])
    db.session.commit()
    plant1_remaining = Stock.query.filter_by(name='Plant1').first()
    print(plant1_remaining.stock)