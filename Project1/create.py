from app import db, app, Stock

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