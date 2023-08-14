from app import db, app, Stock

with app.app_context():
    db.drop_all()
    db.create_all()
    plant1 = Stock(plant_name='Plant1', price=10.00, quantity=10)
    plant2 = Stock(plant_name='Plant2', price=11.25, quantity=10)
    plant3 = Stock(plant_name='Plant3', price=12.50, quantity=10)
    plant4 = Stock(plant_name='Plant4', price=13.75, quantity=10)
    plant5 = Stock(plant_name='Plant5', price=14.00, quantity=10)
    db.session.add_all([plant1, plant2, plant3, plant4, plant5])
    db.session.commit()


