from app import db, app, Users

with app.app_context():
    db.drop_all()
    db.create_all()
    testuser = Users(first_name='Grooty',last_name='Toot') # Extra: this section populates the table with an example entry
    db.session.add(testuser)
    db.session.commit()